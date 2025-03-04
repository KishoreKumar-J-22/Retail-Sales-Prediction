# Required Libraries

import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import *
from streamlit_extras.colored_header import colored_header
from streamlit_extras.keyboard_url import keyboard_to_url
import json as js
import numpy as np
from datetime import date
import pickle
import pymongo as pm
import time 
import pandas as pd
from textblob import TextBlob

class app:
    def model(self):
        st.set_page_config(page_title="Retail Sales Forecast Project", page_icon= ":chart_with_upwards_trend:", layout="wide", initial_sidebar_state="expanded")
        df = pd.read_csv("D:/Final_Capstone/RFS_cleaned_data.csv")
        with st.sidebar:
            selected = option_menu(
                menu_title="Project Work Flow",
                options = ['Intro','Tableau Dashboard','Inferece','Deployment','Feedback'],
                icons = ['mic-fill','bar-chart-line','lightbulb','cloud-upload','chat-left-text-fill'],
                menu_icon= 'alexa',
                default_index = 0
            )

        if selected == 'Intro':
            pass

        elif selected == 'Tableau Dashboard':
            st.markdown("<style>div.block-container{padding-top: 0rem;}</style>", unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([7, 10, 5])
            col1.write('')
            col2.write('')
            col1.write('')
            col2.write('')
            col2.markdown('''<h1 style='font-size: 40px;'><span style = 'color:white;'> Press </sapn>
                          <span style='color:cyan;'>'P'</span> <span style = 'color:white;'> to view the Tableau Dashboard</span></h1>''', unsafe_allow_html=True)
            keyboard_to_url(key='P', url = "https://public.tableau.com/app/profile/kishore.kumar.j/viz/Retail_Sales_Tableau/Dashboard2?publish=yes")


        elif selected == 'Inferece':
            
            
            st.markdown(
            "<h1 style='font-size: 100px; text-align: center;'><span style='color: cyan;'>Regression </span><span style='color: white;'> Model</span> </h1>",
            unsafe_allow_html=True)

            col1, col2, col3 = st.columns([4, 10, 2])
            
            colored_header(label=" ",
                            description=" ",
                            color_name="blue-green-70"
                            )
                
            col1, col2, col3 = st.columns([2, 10, 2])
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")
            col2.write("")

            with col2:
                st.markdown(
                "<h1 style='font-size: 40px;'><span style='color: cyan;'>Store</span><span style='color: white;'>Number </span> </h1>",
                    unsafe_allow_html=True)
                store = st.selectbox("",[1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17,
                                        18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,
                                        35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45])
                
                st.write("")
                st.write("")
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Department  </span><span style='color: white;'> Number </span> </h1>",
                unsafe_allow_html=True)
                dept = st.selectbox("",[1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 16, 17, 18,
                                        19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35,
                                        36, 37, 38, 40, 41, 42, 44, 45, 46, 47, 48, 49, 51, 52, 54, 55, 56,
                                        58, 59, 60, 67, 71, 72, 74, 79, 80, 81, 82, 83, 85, 87, 90, 91, 92,
                                        93, 94, 95, 97, 98, 78, 96, 50, 99, 65, 43, 39, 77])
                

                st.write("")
                st.write("")
                st.markdown("<h1 style='font-size: 40px;'><span style='color: cyan;'>Is </span><span style='color: white;'> Holiday </span> </h1>",
                    unsafe_allow_html=True)
                holiday = st.selectbox("",['False','True'])
                holiday_v = 0 if holiday == 'False' else 1
                #____________________________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown("<h1 style='font-size: 40px;'><span style='color: cyan;'>Temperature  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                temp = st.number_input("", min_value = 1.00, max_value=101.95, value=1.00)
                #____________________________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Fuel Price </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True
                )
                Fuel_Price = st.number_input("", min_value = 2.000, max_value=4.468, value=2.000)
                #____________________________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'> </span><span style='color: cyan;'>Date</span> </h1>",
                    unsafe_allow_html=True)
                Date = st.date_input(label="  ",min_value=date(2010, 2, 5), max_value=date(2013, 7, 26), value=date(2010, 2, 5))
                #____________________________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Size  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                Size =  st.selectbox('',[151315, 202307,  37392, 205863,  34875, 202505,  70713, 155078,
                                                125833, 126512, 207499, 112238, 219622, 200898, 123737,  57197,
                                                    93188, 120653, 203819, 203742, 140167, 119557, 114533, 128107,
                                                152513, 204184, 206302,  93638,  42988, 203750, 203007,  39690,
                                                158114, 103681,  39910, 184109, 155083, 196321,  41062, 118221])
                #____________________________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Type  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                type = st.selectbox("",['A','B','C'])
                type_v = 1 if type == 'A' else (2 if type == 'B' else 3)
                #____________________________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>MarkDown1  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                MarkDown1 = st.number_input("", min_value = -2781.450000, max_value=103184000.980000, value=1.0)
                #____________________________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>MarkDown2  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                MarkDown2 = st.number_input("", min_value = -265.760000, max_value=104519.540000, value=1.0)
                #____________________________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>MarkDown3  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True
                )
                MarkDown3 = st.number_input("", min_value = -179.260000, max_value=149483.310000, value=1.0)
                #____________________________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>MarkDown4  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                MarkDown4 = st.number_input("", min_value =0.220000, max_value=67474.850000, value=0.220000)
                #____________________________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>MarkDown5  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                MarkDown5 = st.number_input("", min_value = -185.170000, max_value=771448.100000, value=1.0)
                #____________________________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>CPI  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True)
                CPI = st.number_input("", min_value =126.064, max_value=228.9764563, value=126.064)
                #____________________________________________________________________________________________
                st.write("")
                st.write("")
                st.markdown(
                    "<h1 style='font-size: 40px;'><span style='color: cyan;'>Unemployment  </span><span style='color: white;'> Value </span> </h1>",
                    unsafe_allow_html=True
                )
                Unemployment = st.number_input("   ",min_value=3.684, max_value=14.313, value=3.684)
                #____________________________________________________________________________________________
                st.write("")
                st.write("")
                st.write("")
                predict_data = [store,dept,holiday_v,temp,Fuel_Price,Date.day,Date.month,Date.year,type_v,Size,MarkDown1,MarkDown2,MarkDown3,MarkDown4,MarkDown5,CPI,Unemployment]
                st.write(predict_data)

                #col1,col2,col3 = st.columns([10,1,10])
                st.write("")
                st.write("")


                with st.container():
                    st.markdown('<div class="center-button">', unsafe_allow_html=True)
                    if st.button("Process"):
                        with open ('D:/Final_Capstone/regressor_model.pkl','rb') as f:
                            model = pickle.load(f)
                        x = model.predict([predict_data])
                        st.markdown(
                            f"<h1 style='font-size: 40px; text-align: center;'><span style='color: cyan;'>Predicted Weekly Sales: </span><span style='color: white;'> {round(x[0],2)}</span> </h1>",
                                unsafe_allow_html=True
                        )

# Object Creation for CLass App

Object = app()
Object.model()
