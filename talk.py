from google.protobuf import message
import streamlit as st
import requests as req
import json
import time
# apikey = "DZZT0d69EJsXngxpx8qCa1wQav5zK5zL" a3rt
apikey = "ca8c2a0b-1bc9-4c25-a708-ff89219689da17d1750d46c2e4"
agent_id = "c8f3c5d2-55c9-4c30-95db-8cd46313a70817d174fff45300"
# api.a3rt.recruit-tech.co.jp
url = "https://www.api-mabo.work/api"

msg = st.text_input("")
if(st.button("送信") and msg):
    my_bar = st.progress(0)
    time.sleep(0.25)
    headers = {'content-type':'text/json'}
    payload = {'utterance':msg}
    apikey = "600293f05aa1c"
    url = 'https://www.chaplus.jp/v1/chat?apikey=' + apikey
    time.sleep(0.5)
    my_bar.progress(25)
    res = req.post(url=url, headers=headers, data=json.dumps(payload))
    my_bar.progress(100)
    restext = res.json()['bestResponse']['utterance']
    st.info(msg)
    st.success(restext)
    options = res.json()["options"]
    option = st.selectbox(
        '他の反応',
        options)
else:
    st.info("会話を入力")