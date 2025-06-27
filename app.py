import os
import subprocess
import streamlit as st

st.set_page_config(page_title="Search to Slides", layout="centered")
st.title("📊 Search to Slides")

query = st.text_input("Enter a topic to generate slides from search:", "")

if st.button("Generate Presentation"):
    if not query.strip():
        st.warning("Please enter a valid query.")
    else:
        st.info("Generating slides... please wait ⏳")

        project_root = os.path.abspath(os.path.dirname(__file__))  # Full path
        cmd = f'npm run generate -- --query "{query}"'

        try:
            result = subprocess.run(
                cmd,
                cwd=project_root,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                encoding='utf-8',
                errors='replace',
                text=True
            )

            if result.returncode != 0:
                st.error("❌ Generation failed!")
                st.code(result.stderr, language='bash')
            else:
                st.success("✅ Presentation generated!")
                presentation_path = os.path.join(project_root, "output", "presentation.html")
                if os.path.exists(presentation_path):
                    with open(presentation_path, "r", encoding="utf-8") as f:
                        html = f.read()

                        st.components.v1.html(
                            html,
                            height=800,
                            scrolling=False
                        )
                else:
                    st.warning("Presentation HTML not found.")

        except Exception as e:
            st.exception(e)