import validators
import streamlit as st
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import YoutubeLoader,UnstructuredURLLoader


#Set Page Congig

st.set_page_config(
    page_title="Langchain Youtube Text Summarizer",
    page_icon="📺"

)

st.title("📺 Langchain: Summarize Text from YouTube or Websites")
st.subheader('Summarize URL')


#Getting API KEY & YOUTUBE URL WEBSITE

with st.sidebar:
    model_name = st.selectbox("Model", [
    "llama3-8b-8192", 
    "mixtral-8x7b-32768", 
    "gemma-7b-it"
])
    
    groq_api_key = st.text_input("Groq API key", value="", type="password")

generic_url = st.text_input("URL", label_visibility="collapsed")

#MODEL LOAD


llm = ChatGroq(model=model_name, api_key=groq_api_key)

prompt_template = ''' 
  Provide a summary of the following content about 300 words:
  Content:{text}

'''

prompt = PromptTemplate(template=prompt_template,input_variables=['text'])


if st.button("✍🏻 Summarize "):
    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")
    elif not validators.url(generic_url):
        st.error("Please enter a valid url. it can may be a Youtube video…")
    else:
        try:
            with st.spinner("Waiting.."):
                if "youtube.com" in generic_url:
                    loader=YoutubeLoader.from_youtube_url(generic_url,add_video_info=True)
                else:
                    loader=UnstructuredURLLoader(urls=[generic_url],ssl_verify=False,headers={"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36"})
                docs=loader.load()
                chain= load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                output_summary=chain.run(docs)

                st.success(output_summary)
        except Exception as e:
            st.error(f"Exception: {e}")
