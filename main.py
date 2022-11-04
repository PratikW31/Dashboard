import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.set_option('deprecation.showPyplotGlobalUse', False)

df=pd.read_csv("Programming.csv")
st.title("Programming Languages")
df=df.set_index("Date")

listcolumns=list(df.columns)
defaultx=listcolumns.index("Python")
selectst=st.selectbox("Select Column",listcolumns,index=defaultx)

if selectst:
 df=df[selectst]
 df=df.reset_index()

fig=px.line(df,x="Date",y=selectst)
st.plotly_chart(fig,use_container_width=True)

col1,col2,col3=st.columns(3)

with col1:
 maxvalue=df[selectst].max()
 st.write("Max",df[df[selectst]==maxvalue])

with col2:
 minvalue=df[selectst].min()
 st.write("Min",df[df[selectst]==minvalue])

with col3:
 st.write("Last",df[df["Date"]=="January 2022"])

#maxvalue2=dosya[selectst].max()
#lastdf=dosya[dosya["Date"]=="January 2022"]
#lastvalue2=lastdf[selectst]
#lastvalues2=lastvalue2.values


newdf=pd.read_csv("C:/Users/asus/Desktop/DATA/Programming.csv")

listdates=list(newdf["Date"])
listdates.insert(0,"All")

defaultix=listdates.index("January 2022")
datest=st.selectbox("Select Date",listdates,index=defaultix)

if datest!="All":
 newdf=newdf[newdf["Date"]==datest]
newdf=newdf.set_index("Date")
columnslist=list(newdf.columns)
columnslistst=st.multiselect("Select Columns",columnslist,default=columnslist)

if columnslistst:
 newdf=newdf[columnslistst]
 maxvalues=newdf[columnslistst].max()
 fig = px.pie(newdf, values=maxvalues, names=columnslistst,height=600)

 #fig=px.bar(newdf,x=columnslistst,y=maxvalues)

 st.plotly_chart(fig,use_container_width=True)
newdf=newdf.reset_index()
st.dataframe(newdf)