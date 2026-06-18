from typing import TypedDict

from langgraph.graph import StateGraph, END

from cv_analyzer import analyze_cv


class CVState(TypedDict):
    cv_text: str
    structure_analysis: str
    ats_analysis: str
    summary: str
    final_feedback: str


def analyze_structure(state):
    template = """
Anda adalah HR profesional Indonesia.

Jawablah seluruh output menggunakan Bahasa Indonesia formal.

Jangan menggunakan Bahasa Inggris kecuali nama teknologi seperti Python, SQL, Machine Learning, atau NLP.

Analisis struktur CV berikut.

Berikan:
1. Kelebihan struktur
2. Kekurangan struktur

CV:
{cv_text}
"""

    result = analyze_cv(
        template,
        {
            "cv_text": state["cv_text"]
        }
    )

    return {
        "structure_analysis": result
    }


def analyze_ats(state):
    template = """
Anda adalah ATS Reviewer profesional Indonesia.

Jawablah seluruh output menggunakan Bahasa Indonesia formal.

Jangan menggunakan Bahasa Inggris kecuali nama teknologi seperti Python, SQL, Machine Learning, atau NLP.

Analisis CV berikut menggunakan rubric penilaian.

Kriteria:

1. Format CV (0-20)
2. Informasi Kontak (0-10)
3. Skill dan Teknologi (0-20)
4. Pengalaman/Proyek (0-30)
5. Pendidikan (0-20)

Hitung setiap komponen.

Output HARUS menggunakan format berikut:

ATS SCORE: [total]/100

FORMAT: [nilai]/20
KONTAK: [nilai]/10
SKILL: [nilai]/20
PENGALAMAN: [nilai]/30
PENDIDIKAN: [nilai]/20

ALASAN:
[Tuliskan dalam bahasa indonesia]

SARAN:
[Tuliskan dalam bahasa indonesia]

CV:
{cv_text}
"""

    result = analyze_cv(
        template,
        {
            "cv_text": state["cv_text"]
        }
    )

    return {
        "ats_analysis": result
    }

def generate_summary(state):
    template = """
Anda adalah HR profesional Indonesia.

Jawablah seluruh output menggunakan Bahasa Indonesia formal.

Jangan menggunakan Bahasa Inggris kecuali nama teknologi seperti Python, SQL, Machine Learning, atau NLP.

Buat ringkasan kandidat berdasarkan CV berikut.

Berikan:

1. Profil singkat kandidat
2. Bidang utama kandidat
3. Skill utama kandidat
4. Potensi karir kandidat

Maksimal 150 kata.

CV:
{cv_text}
"""

    result = analyze_cv(
        template,
        {
            "cv_text": state["cv_text"]
        }
    )

    return {
        "summary": result
    }

def generate_feedback(state):
    template = """
Anda adalah konsultan karir profesional Indonesia.

Jawablah seluruh output menggunakan Bahasa Indonesia formal.

Berdasarkan hasil berikut:

Summary:
{summary}

Struktur:
{structure}

ATS:
{ats}

Berikan:

1. Kelebihan kandidat
2. Kekurangan kandidat
3. Rekomendasi perbaikan CV
4. Rekomendasi karir yang sesuai
"""

    result = analyze_cv(
        template,
        {
        
            "summary": state["summary"],
            "structure": state["structure_analysis"],
            "ats": state["ats_analysis"]
        
        }
    )

    return {
        "final_feedback": result
    }


builder = StateGraph(CVState)

builder.add_node("structure", analyze_structure)
builder.add_node("ats", analyze_ats)
builder.add_node("summary", generate_summary)
builder.add_node("feedback", generate_feedback)

builder.set_entry_point("structure")

builder.add_edge("structure", "ats")
builder.add_edge("ats", "summary")
builder.add_edge("summary", "feedback")
builder.add_edge("feedback", END)

graph = builder.compile()