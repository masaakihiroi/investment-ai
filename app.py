import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("投資分析AI")

uploaded_file = st.file_uploader("CSVファイルをアップロードしてください")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("データの確認")
    st.dataframe(df)

    if "損益" in df.columns:
        st.write("損益の合計")
        st.write(df["損益"].sum())

        win_rate = (df["損益"] > 0).mean() * 100
        st.write("勝率")
        st.write(f"{win_rate:.1f}%")

        st.write("損益のグラフ")
        fig, ax = plt.subplots()
        df["損益"].plot(kind="bar", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("「損益」という列が見つかりません")