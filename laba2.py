import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import numpy as np
from sympy import *
import math
from opt_methods import hook_jeeves
import pandas as pd

with st.sidebar:
    selected = option_menu(
        menu_title="Hub",
        options = [
                   "Цель работы", 
                   "Исходное задание на исследование", 
                   "Таблицы с результатами исследований по каждому методу", 
                   "График зависимости количества вычислений целевой функции от логарифма задаваемой точности E", 
                   "Анализ полученных результатов и выводы"
                   ],
        default_index=0,
        icons=["info-circle-fill", "info-square", "table", "graph-up", "database-check"],
        styles={
            "nav-link-selected": {'background-color': 'purple'},
        },
        )
    
if selected == "Цель работы":
    st.title(f"{selected}") 
    st.header("Изучение, анализ и программная реализация алгоритмов многомерной оптимизации: метода Гаусса-Зейделя, метода наискорейшего спуска, метода Хука и Дживса, метода Розенброка")

if selected == "Исходное задание на исследование":
    st.title(f"{selected}")
    st.header("Вариант - 9")
    st.subheader("Функция:")
    st.latex("f(x) = x^5 - x^2")

if selected == "Таблицы с результатами исследований по каждому методу":

    st.title("Таблицы с результатами исследований по каждому методу")

    methods = {
        "Метод Хука и Дживса": 1,
        "Метод Гаусса-Зейделя": 2,
        "Метод Розенброка": 3,
        "Метод быстрого спуска": 4
    }

    method = st.selectbox("Выберите метод", tuple(methods.keys()))

    if method == "Метод Хука и Дживса":
        x_0 = st.number_input('Введите x0', step = 0.01)
        y_0 = st.number_input('Введите y0', step = 0.01)
        x_start = np.array([x_0, y_0])

        st.write(x_start)

        delta = st.number_input('Введите параметр delta', step = 0.0001)
        st.write(delta)
        epsilon = st.number_input('Введите параметр epsilon', step = 0.0001)
        st.write(epsilon)


        if st.button("Calculate"):
            x, cel, df = hook_jeeves(x_start, delta, epsilon)

            st.write("Значение целевой функции")
            st.latex(cel)
            st.write("Значение x")
            st.latex(x)
            st.write("Таблица с итерациями")
            st.write(df)

    if method == "Метод Гаусса-Зейделя":

        x_0 = st.number_input('Введите x0', step = 0.01)
        y_0 = st.number_input('Введите y0', step = 0.01)
        x_start = np.array([x_0, y_0])

        st.write(x_start)

        n = st.number_input('Введите параметр n', step = 1)
        st.write(n)
        epsilon = st.number_input('Введите параметр epsilon', step = 0.0001)
        st.write(epsilon)

        if st.button("Calculate"):
            x, cel, df = gauss_zeidel(x_start, n, epsilon)

            st.write("Значение целевой функции")
            st.latex(cel)
            st.write("Значение x")
            st.latex(x)
            st.write("Таблица с итерациями")
            st.write(df)

    if method == "Метод Розенброка":

        x_0 = st.number_input('Введите x0', step = 0.01)
        y_0 = st.number_input('Введите y0', step = 0.01)
        x_start = np.array([x_0, y_0])

        st.write(x_start)

        alpha = st.number_input('Введите параметр alpha', step = 1)
        st.write(alpha)
        epsilon = st.number_input('Введите параметр epsilon', step = 0.0001)
        st.write(epsilon)

        if st.button("Calculate"):
            x, cel, df = rosenbrock(x_start, alpha, epsilon)

            st.write("Значение целевой функции")
            st.latex(cel)
            st.write("Значение x")
            st.latex(x)
            st.write("Таблица с итерациями")
            st.write(df)

    if method == "Метод быстрого спуска":

        x_0 = st.number_input('Введите x0', step = 0.01)
        y_0 = st.number_input('Введите y0', step = 0.01)
        x_start = np.array([x_0, y_0])

        st.write(x_start)

        epsilon = st.number_input('Введите параметр epsilon', step = 0.0001)
        st.write(epsilon)

        if st.button("Calculate"):
            x, cel, df = rapid_descent(x_start, epsilon)

            st.write("Значение целевой функции")
            st.latex(cel)
            st.write("Значение x")
            st.latex(x)
            st.write("Таблица с итерациями")
            st.write(df)

    