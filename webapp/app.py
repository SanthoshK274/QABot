import streamlit as st
from qabot import loaddoc,response
def main():
    st.title("QABot")
    uploadedfile=st.file_uploader("Upload PDF", type=["pdf"])

    if uploadedfile is not None:
        doctext=loaddoc(uploadedfile)
        st.success("Document uploaded successfully!")
        question=st.text_input("Ask a question about the document:")
        
        if st.button("Get Answer"):
            if question:
                answer=response(question,doctext)
                st.write("Answer:", answer)
            else:
                st.warning("Please enter a question.")

if __name__=="__main__":
    main()