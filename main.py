import streamlit as st
import pickle
from datetime import datetime

st.title("Flight Price Prediction Application")
#Airline___________________________________________________________________________________________________
Airline=st.sidebar.selectbox("Airline",(None,"SpiceJet","Vistara","Indigo","AirAsia","GO_FIRST","Air_India"))
Airline_dict={'AirAsia':0,'Indigo':1,'GO_FIRST':2,'SpiceJet':3,'Air_India':4 ,'Vistara':5}
#Source_City___________________________________________________________________________________________________
Source=st.sidebar.selectbox("Source",(None,"Bangalore","Chennai","Delhi","Kolkata","Mumbai","Hyderabad"))
Source_dict={'Delhi':0,'Hyderabad':1,'Bangalore':2,'Mumbai':3,'Kolkata':4,'Chennai':5}
#Depature_Time___________________________________________________________________________________________________
Depature_Time=st.sidebar.selectbox("Depature Time",(None,"Early_Morning","Morning", 'Afternoon',"Evening","Night","Late_Night"))
Depature_Time_dict={'Early_Morning':0,'Morning':1,'Afternoon':2,'Evening':3,'Night':4,'Late_Night':5}
#Stop___________________________________________________________________________________________________
Stop=st.sidebar.selectbox("Stop",(None,"zero","one","two","two_or_more"))
Stop_dict={'zero':0,'one':1,'two':2,'two_or_more':3}
#Arrival_Time___________________________________________________________________________________________________
Arrival_Time=st.sidebar.selectbox("Arrival Time",(None,"Early_Morning","Morning", 'Afternoon',"Evening","Night","Late_Night"))
Arrival_Time_dict={'Early_Morning':0,'Morning':1,'Afternoon':2,'Evening':3,'Night':4,'Late_Night':5}
#Destination___________________________________________________________________________________________________
Destination=st.sidebar.selectbox("Destination",(None,"Bangalore","Chennai","Delhi","Kolkata","Mumbai","Hyderabad"))
Destination_dict={'Delhi':0,'Hyderabad':1,'Bangalore':2,'Mumbai':3,'Chennai':4,'Kolkata':5}
#Class___________________________________________________________________________________________________
Class=st.sidebar.selectbox("Class",(None,"Economy","Business"))
Class_dict={'Economy':0,'Business':1}
#Days_After____________________________________________________________________________________________________
Date=st.sidebar.date_input("Departure Date")
daY_diff=datetime.strptime(str(Date),"%Y-%m-%d")-datetime.today()
daY_diff=int(daY_diff.days+1)
#Load the saved model___________________________________________________________________________________________________

f=[Airline,Source,Depature_Time,Stop,Arrival_Time,Destination,Class,daY_diff]
if None not in f and st.button("Predict"):
    Features=[Airline_dict[Airline],Source_dict[Source],Depature_Time_dict[Depature_Time],Stop_dict[Stop],Arrival_Time_dict[Arrival_Time],Destination_dict[Destination],Class_dict[Class],daY_diff]
    
    
    Model=pickle.load(open('LinearModel.pkl','rb'))
    prediction=Model.predict([Features])[0]
    st.title(f"Your Flight Price is Rs.{round(prediction)}/-")
