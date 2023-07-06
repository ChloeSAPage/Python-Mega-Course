import streamlit as st

st.set_page_config(layout="wide")

column1, column2 = st.columns(2)

with column1:
    st.image("images\graduation photo - Copy.jpg", width = 400)

with column2:
    st.title("Chloe Page")
    content = """
Hi, I'm Chloe! I graduated in 2022 with a 2:1 in BSc Microbiology, where i gained many invaluable skills and honed my biological and laboratory knowledge. 
When I'm not in the lab, I'm diving into the world of coding. I'm a beginner, and am currently taking the "Python Mega Course" on Udemy. 
I'm excited to leverage my scientific background and newfound coding skills to contribute to the biotech field. 
Beyond my academic and technical pursuits, I'm an avid member of the Microbiology Society, where I attend talks to stay up-to-date with the latest advancements. In my downtime, you can find me building PCs, indulging in science fiction and fantasy literature, or binge-watching related TV shows.
I'm currently working on building my portfolio, so stay tuned for updates! 
If you have any questions or exciting opportunities in the biotech world, feel free to reach out. Let's connect and explore the intersection of biotech and coding together!
"""
    st.info(content)