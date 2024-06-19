import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain_community.llms import CTransformers
# Response Function

def getLLamaResponse(input_text,no_words,blog_style):

    # Calling Llama Model using Ctransformers

    llm = CTransformers(model='/Users/chaitanyakakade/Desktop/Llama 2 LLM Project/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens':256,
                                'temperature':0.01})
    
    ## Prompts

    template='''
        Write a blog for {blog_style} job 
        profile for a topic {input_text} within {no_words} words
        '''
    prompt=PromptTemplate(input_variables=["blog_style","input_text",'no_words'],
                          template=template)

    # response grenerations

    responses = llm(prompt.format(blog_style=blog_style,input_text=input_text,no_words=no_words))
    print(responses)
    return responses



st.set_page_config(page_icon='🪶',
                page_title="Blog Generation",
                layout='centered',
                initial_sidebar_state='collapsed')

st.header("Quantum Quills 🪶")

input_text=st.text_input("Topic Name ")

column1,column2=st.columns([5,5])

with column1:
    no_words=st.text_input("No of Words")
with column2:
    blog_style=st.selectbox('Writing the blog for',
                            ('Fun','General','Professional'),index=0)
    
submit=st.button("Generate")


if submit:
    st.write(getLLamaResponse(input_text,no_words,blog_style))