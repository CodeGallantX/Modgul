import streamlit as st
from fpdf import FPDF
import datetime
import io

# ========== Define the PDF structure ==========
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, 'GST 112: Nigerian Peoples and Culture', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 5, 'An In-Depth Historical and Cultural Analysis', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()} / {{nb}}', 0, 0, 'C')
    
    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, title, 0, 1, 'L', 1)
        self.ln(2)
    
    def chapter_body(self, body):
        self.set_font('Arial', '', 11)
        self.multi_cell(0, 8, body)
        self.ln(5)
    
    def add_timeline(self, events):
        self.set_font('Arial', 'B', 10)
        self.cell(0, 10, "Historical Timeline:", 0, 1)
        self.set_font('Arial', '', 10)
        for year, event in events:
            self.multi_cell(0, 6, f"• {year}: {event}")
        self.ln(5)
    
    def add_quote(self, text, author):
        self.set_font('Arial', 'I', 10)
        self.multi_cell(0, 6, f'"{text}"')
        self.set_font('Arial', '', 10)
        self.cell(0, 6, f'- {author}', 0, 1, 'R')
        self.ln(5)

# ========== Story content ==========
story = {
    "Chapter One: The Beginning — Before the White Man Came (Pre-1472)": """\
The story of Nigeria begins long before European contact, with archaeological evidence showing human habitation dating back to at least 9000 BCE. The Nok culture (1500 BCE - 200 CE) emerged in central Nigeria, producing Africa's earliest terracotta sculptures and evidence of iron smelting. These life-sized figurines with intricate hairstyles and jewelry suggest a sophisticated society with specialized artisans.

In southwestern Nigeria, the Yoruba civilization flourished with the rise of Ife around 1000 CE. Oral traditions speak of Oduduwa descending from the heavens with a chain to establish the first Yoruba kingdom. Ife's naturalistic bronze and terracotta heads, created using the lost-wax technique, remain some of Africa's most refined artworks. By the 14th century, Oyo emerged as the dominant Yoruba state, developing a complex political system with the Alaafin (king) balanced by the Oyo Mesi council and the Bashorun prime minister. The Oyo cavalry, using horses acquired through trans-Saharan trade, created an empire stretching into modern Benin and Togo.

The Benin Kingdom (1180-1897) to the southeast developed equally impressive bronze casting traditions. Under Oba Ewuare (1440-1473), Benin expanded its walls - described as the world's largest earthworks before the mechanical age. The obas maintained a royal guild system producing the famous Benin Bronzes that later fascinated Europe.

Northern Nigeria saw the rise of Hausa city-states (Kano, Katsina, Zaria) from the 11th century, thriving as centers of trans-Saharan trade. The Kanem-Bornu Empire (700-1900), centered around Lake Chad, became a Islamic learning hub under Mai Idris Alooma (1571-1603) who established diplomatic relations with Tripoli.

In southeastern Nigeria, the Igbo maintained a decentralized society organized around village democracies. The 9th century Igbo Ukwu archaeological site revealed sophisticated bronze artifacts using local copper sources, indicating advanced metallurgy before outside influence.
""",
    "Chapter Two: A Tower of Babel — Languages Across the Land": """\
Nigeria's linguistic landscape presents one of the world's most complex tapestries. With over 500 languages (about 25% of Africa's total), Nigeria surpasses all other African nations in linguistic diversity. This variety stems from millennia of migrations, trade contacts, and geographical barriers like the Niger River and Jos Plateau.

The Niger-Congo family dominates southern Nigeria. Yoruba (Èdè Yorùbá) traces its literary tradition to the 17th century when Muslim clerics began writing it in Ajami script. The language's tonal nature (three pitch levels) allows for proverbs like "Ọmọdé gbọ́n, àgbà gbọ́n, la fi dá Ilẹ̀-Ifẹ̀" (Both child and elder are wise, hence the founding of Ife). Igbo (Ásụ̀sụ̀ Ị̀gbò) shows remarkable dialectal variation, with at least 20 mutually intelligible dialects. The 19th century Nsibidi ideographic writing system, used by Ekpe secret societies, represents one of Africa's indigenous scripts.

Hausa (Harshen Hausa), the largest Chadic language, became the lingua franca of West African trade. Its Ajami writing flourished in the Sokoto Caliphate, producing works like the 19th century Wakar Muhammadu. Colonial officer Rupert East later developed the Boko (Latin-based) script in the 1930s.

Language conflicts emerged during colonial rule when the British promoted Hausa in the north but encountered resistance in the south. The 1952-53 constitutional crisis partly stemmed from northern fears that English-medium education would disadvantage Hausa speakers. Post-independence, the language question remains contentious, with the 1977 National Policy on Education's mother-tongue provisions poorly implemented. Today, about 50 Nigerian languages face extinction, including Defaka (spoken by <200 people in Rivers State) and Akum (a Plateau language with <100 speakers).

Pidgin English (Naijá) has become the true national lingua franca, evolving distinct varieties like Lagos "Broken" and Delta "Waffi." Its vocabulary borrows from Portuguese ("sabi" - to know), indigenous languages ("wahala" - trouble), and creative neologisms ("ajebutter" - privileged youth).
"""
}

# ========== Streamlit UI ==========
st.set_page_config(page_title="GST 112 PDF Generator", page_icon=":books:", layout="centered")

st.title("GST 112: Nigerian Peoples and Culture")
st.subheader("Generate a beautifully formatted PDF")

st.write("Click the button below to generate the full PDF document for GST 112.")

if st.button("Generate PDF"):
    # Create PDF in memory
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()

    # Cover Page
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(0, 40, '', 0, 1)
    pdf.cell(0, 10, 'GST 112:', 0, 1, 'C')
    pdf.cell(0, 10, 'Nigerian Peoples and Culture', 0, 1, 'C')
    pdf.set_font('Arial', '', 14)
    pdf.cell(0, 30, '', 0, 1)
    pdf.cell(0, 10, 'Comprehensive Historical Archive', 0, 1, 'C')
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 5, f'Generated on: {datetime.datetime.now().strftime("%Y-%m-%d")}', 0, 1, 'C')

    # Table of Contents
    pdf.add_page()
    pdf.chapter_title('Table of Contents')
    chapters = [
        "Chapter One: The Beginning — Before the White Man Came (Pre-1472)",
        "Chapter Two: A Tower of Babel — Languages Across the Land",
        "Chapter Three: Forged in Fire — From Kingdoms to Colonies (1472-1960)",
        "Chapter Four: Of Trade, Wealth, and Survival — The Economy of a People",
        "Chapter Five: Nation in Turmoil — Challenges to Unity (1960-Present)",
        "Chapter Six: Guardians of Justice — The Role of the Judiciary",
        "Chapter Seven: Norms, Values, and the Soul of a People"
    ]
    for i, chapter in enumerate(chapters, start=1):
        pdf.cell(0, 10, f'{i}. {chapter}', 0, 1)
    pdf.ln(10)
    pdf.add_quote("Until the lions have their own historians, the history of the hunt will always glorify the hunter.", "Chinua Achebe")

    # Content
    pdf.add_page()
    for chapter, content in story.items():
        pdf.chapter_title(chapter)
        pdf.chapter_body(content)

        if chapter.startswith("Chapter One"):
            pdf.add_timeline([
                ("9000 BCE", "Earliest evidence of human habitation at Iwo Eleru rock shelter"),
                ("1500 BCE", "Nok culture emerges with iron smelting and terracotta art"),
                ("1000 CE", "Yoruba civilization rises in Ife"),
                ("1180 CE", "Benin Kingdom established"),
                ("11th century", "Hausa city-states thrive in northern Nigeria")
            ])
    
    # Save to BytesIO
    buffer = io.BytesIO()
    pdf.output(buffer)
    buffer.seek(0)

    # Download button
    st.download_button(
        label="Download PDF",
        data=buffer,
        file_name="gst112_nigerian_peoples_and_culture.pdf",
        mime="application/pdf"
    )

st.info("Built by John. Stay scholarly, stay savage!")
