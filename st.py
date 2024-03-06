import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
def loss(w):
    return w**2+3

def derivative(w):
    return 3* (w)

def step(w, _lambda):
    coord = w - _lambda * derivative(w)
    return coord , loss(w)

def get_minima(w_0, eps, _lambda): 
    loss_values=[loss(w_0)]
    w=[w_0]
    for i in range(100000): 
        s=step(w_0,_lambda)
        #print(round(s[0]),round(s[1],4))
        if abs(s[0]-w_0) <eps:
            break
        w_0=s[0]
        w+=[w_0]
        loss_values+=[s[1]]

    return w, loss_values

def giveplot(w,l,alp):
    fig, axs = plt.subplots(2, 1, sharex=True)

    # Первый график
    axs[0].plot(w, label='измененое весов')
    axs[0].set_ylabel('веса')
    axs[0].legend()

    # Второй график
    axs[1].plot(l, label='изменение потерь')
    axs[1].set_xlabel(f'Шаги, alpha ={alp}')
    axs[1].set_ylabel('лоссы')
    axs[1].legend()

    st.pyplot(fig)

def main():
    # Создание формы с ползунком
    parameter_value = st.slider('Выберите параметр', 0.001, 1.0, 0.5, 0.001)

    # Отображение графика в зависимости от значения ползунка
    
    try:
        w,l=get_minima(9,0.001,parameter_value)
        giveplot(w,l, parameter_value)
    except:
        st.title("Функция взорвалась!!")
if __name__ == '__main__':
    main()
