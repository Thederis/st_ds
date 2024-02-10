# 1/10   1. Введение. Функции активации
<div class="main-block">
<h2>Введение</h2>
<p>В этом модуле мы поговорим о следующем:</p>
<ul class="list">
<li>функциях активации;</li>
<li>инициализации;</li>
<li>batch нормализации;</li>
<li>dropout регуляции;</li>
<li>градиентном спуске;</li>
<li>стохастическом градиентном спуске;</li>
<li>матричных операциях.</li>
</ul>
<h2>Функции активации</h2>

<div class="term"><b>Функция активации</b> нейрона определяет выходной сигнал, который в свою очередь определяется входным сигналом или набором входных сигналов. Функцию активации используют, чтобы получить выходные данные узла.</div>
<p>Функции активации делятся на два типа:</p>
<ul class="list">
<li>линейные функции активации;</li>
<li>нелинейные функции активации.</li>
</ul>
<div class="term"><b>Сигмоида (Sigmoid)</b> — возрастающая нелинейная функция, имеющая форму буквы «S». В нейронных сетях она используется потому, что позволяет усиливать слабые сигналы.</div>
<p>Проблемы Sigmoid активации:</p>
<ul class="list">
<li>Нейроны с сигмоидой могут насыщаться и приводить к угасающим градиентам.</li>
<li>Не центрированы в нуле.</li>
<li>Дорого вычислять.</li>
</ul>
<p style="text-align: center;"><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block@DSLIGHT_DL_4_1_1.png" style="width: 800px;"></p>
<div class="term"><strong>Функция Tanh</strong> похожа на сигмоиду, но её преимущество состоит в том, что отрицательные входные данные будут отображаться строго отрицательными, а нулевые входные данные будут отображаться вблизи нуля.</div>
<p>Характеристики Tanh активации:</p>
<ul class="list">
<li>Центрирована в нуле.</li>
<li>Но все ещё как сигмоида.</li>
</ul>
<p style="text-align: center;"><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block@DSLIGHT_DL_4_1_2.png" style="width: 800px;"></p>
<div class="term"><b>ReLU (rectified linear unit) </b>является наиболее часто используемой функцией активации в мире, т. к. она используется практически во всех свёрточных нейронных сетях или для deep learning.</div>
<p>Характеристики ReLU активации:</p>
<ul class="list">
<li>Быстро считается.</li>
<li>Градиенты не угасают при x > 0 </li>
<li>Не центрирована в нуле.</li>
<li>Если не было активации — не будет обновления.&nbsp;</li>
</ul>
<p style="text-align: center;"><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block@DSLIGHT_DL_4_1_3.png" style="width: 800px;"></p>
<div class="term"><b>Leaky ReLU</b> является попыткой решить проблему выхода из строя ReLU.</div>
<p>Характеристики Leaky ReLU активации:</p>
<ul class="list">
<li>Всегда будут обновления.</li>
<li>Примерно центрирована в нуле.</li>
<li>a ≠ 1.</li>
</ul>
<p style="text-align: center;"><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block@DSLIGHT_DL_4_1_4.png" style="width: 800px;"></p>
<div class="term"><b>Функция активации ELU</b> (Exponential Linear Unit), по результатам исследований, быстрее сводит к нулю и даёт более точные результаты.</div>
<p>В отрицательной части аргументов использует экспоненту.</p>
<p style="text-align: center;"><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block@DSLIGHT_DL_4_1_5.png" style="width: 800px;"></p>
<p>Характеристики ELU:</p>
<ul class="list">
<li>Примерно центрирована в нуле;</li>
<li>Сходимость быстрее ReLU.</li>
</ul>
<p style="text-align: center;"><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block@DSLIGHT_DL_4_1_6.png" style="width: 500px;"></p>
<h3>Дополнительные материалы</h3>
<div class="color-container container-flex orange-container">
<div class="container-icon"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 26 26" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M12.9998 17.8658C10.971 15.8359 7.91272 15.4628 5.50472 16.7463C4.82144 17.1105 3.99609 16.6613 3.99609 15.887V6.79116C3.99609 6.1549 4.29022 5.54264 4.80843 5.17349C7.29447 3.40075 10.7689 3.62985 12.9998 5.86078C15.2308 3.62985 18.7052 3.40075 21.1913 5.17349C21.7095 5.54264 22.0036 6.1549 22.0036 6.79116V15.887C22.0036 16.6613 21.1782 17.1115 20.495 16.7463C18.087 15.4628 15.0287 15.8359 12.9998 17.8658Z" stroke="#00EEEE" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M5.50391 20.8845C7.91191 19.601 10.9702 19.9741 12.999 22.004C15.0279 19.9741 18.0861 19.601 20.4941 20.8845" stroke="#00EEEE" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M13.0002 17.8663V5.86133" stroke="#00EEEE" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </svg></div>
<span><a href="https://arxiv.org/pdf/1511.07289.pdf" target="_blank" rel="noopener">Fast and accurate deep network learning by exponential linear units (ELUs)</a> </span></div>
</div>

# 2. Инициализация весов

<div class="main-block">

<p>Нейронные сети нельзя инициализировать нулевыми весами, т.к. в этом случае появляется эффект симметрии и, как следствие, сеть станет менее мощной.</p>
<h2>Нейрон и дисперсия до активации</h2>
<p>Если у каждого входа нейросети среднее равно 0, и мы генерируем веса независимо от входов, то это нам гарантирует, что <strong>среднее нейрона до активации тоже будет равно 0.&nbsp;</strong></p>
<p>Но дисперсия может расти, и это замедлит сходимость.</p>
<p style="text-align: center;"><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block@DSLIGHT_DL_4_2_1.png" style="width: 650px;"></p>
<div class="term"><b>Дисперсия суммы некоррелированных величин</b> — это сумма дисперсий, слагаемые некоррелированы, потому что веса, которые мы генерируем, независимы.</div>
<h2>Сходимость</h2>
<p><span>Гиперболический тангенс для маленьких функций (около 0) похож на линейную функцию, то есть наши ранние выкладки примерно верны, и это означает, что т. к. мы гарантируем одинаковую дисперсию на &nbsp;разных слоях нейросети, то выход будет распределен примерно одинаково после применения функции активации и, следовательно, градиенты будут в примерно одинаковом масштабе — этот факт позволит <b>ускорить сходимость.<o:p></o:p></b></span></p>
<p style="text-align: center;"><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block@DSLIGHT_DL_4_2_2.png" style="width: 700px;"></p>
<h3>Дополнительные материалы</h3>
<div class="color-container container-flex orange-container">
<div class="container-icon"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 26 26" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M12.9998 17.8658C10.971 15.8359 7.91272 15.4628 5.50472 16.7463C4.82144 17.1105 3.99609 16.6613 3.99609 15.887V6.79116C3.99609 6.1549 4.29022 5.54264 4.80843 5.17349C7.29447 3.40075 10.7689 3.62985 12.9998 5.86078C15.2308 3.62985 18.7052 3.40075 21.1913 5.17349C21.7095 5.54264 22.0036 6.1549 22.0036 6.79116V15.887C22.0036 16.6613 21.1782 17.1115 20.495 16.7463C18.087 15.4628 15.0287 15.8359 12.9998 17.8658Z" stroke="green" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M5.50391 20.8845C7.91191 19.601 10.9702 19.9741 12.999 22.004C15.0279 19.9741 18.0861 19.601 20.4941 20.8845" stroke="green" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M13.0002 17.8663V5.86133" stroke="green" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </svg></div>
<ul class="list">
<li><a href="https://slideplayer.com/slide/7341917/" target="_blank" rel="noopener">Computacion Inteligente Derivative-Based Optimization</a></li>
<li><a href="https://en.wikipedia.org/wiki/Variance" target="_blank" rel="noopener">Sum of uncorrelated variables (Bienaymé formula)</a></li>
<li><a href="http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf" target="_blank" rel="noopener">Understanding the difficulty of training deep feedforward neural networks</a></li>
</ul>
</div>
</div>

# 3. Влияние learning rate и масштаба признаков на сходимость

[Скачать ноутбук к скринкасту](https://lms-cdn.skillfactory.ru/assets/courseware/v1/d0571757d0b1bc88377a888adbcd4e8b/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/dl_mod_4_3.ipynb)

[Перейти к файлу в системе(относительный путь)](./dl_mod_4_3.ipynb)

[Перейти к файлу в системе(полный путь)](../../../../../../../home/denis/Документы/Cource_on_DS/IDE/learning/Deep_learning_in_Data_Sciences/dl_mod_4_3.ipynb)

<a href="file:///home/denis/Документы/Cource_on_DS/IDE/learning/Deep_learning_in_Data_Sciences/dl_mod_4_3.ipynb">Перейти к файлу в системе(HTML-ссылка)</a>

В этом видео рассмотрим, как влияет масштаб признаков в линейной регрессии на сходимость градиентных методов.

Начнём с импорта библиотек. Здесь нам понадобится tensorflow для визуализации процесса градиентного спуска и вспомогательные функции, которые будут отрисовывать анимацию.

Задача регрессии:

У нас есть два признака: $x_1, x_2$ , на которых настроена линейная модель для предсказания $y$.

Лосс на одном объекте: $l=(x_1w_1+x_2w_2-y)^2$
Среднеквадратичное отклонение будем рисовать в пространстве параметров при помощи линий уровня. Линия уровня — это множество точек, на которых функция принимает одно и то же значение.

<center> <img src=https://lms-cdn.skillfactory.ru/assets/courseware/v1/80b18a9236e3083b5fe31942cb8d683a/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/MAT_3_unit_02.jpg>
</center>

Глядя на линии уровня, мы можем представить, как устроена трёхмерная поверхность функции двух переменных $w_1$ и $w_2$. Красная точка на рисунке — это оптимальный набор параметров.

Рассмотрим, как выглядят матрицы $W_1$ и $W_2$. Для расчёта функции потерь, вытянем их в вектор.

```python
Z = np.mean((x.dot(np.vstack([W1.ravel(), W2.ravel()])) - y)**2, axis=0).reshape(W1.shape)
```

Рассмотрим, как изменятся линии уровня, если ось  умножим на коэффициент 2.

```python
x[:, 0] *= 2  # признак x1 в x_scale раз больше (создаёт долины в лоссе)
```

<center> <img src=https://lms-cdn.skillfactory.ru/assets/courseware/v1/938da5668e0b82ce3acde18177ff0b1a/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/MAT_3_unit_04.jpg>
</center>

Эллипс сузился по горизонтальной оси.

Если мы будем увеличивать масштаб $x_1$, это будет сплющивать ось $w_1$ на графике линий уровня. Если $x_1$ — большое число, то при небольшом изменении $w_1$ лосс изменится сильно.

Можно посчитать градиенты функций потерь по $w_1$ и $w_2$:

$$\frac{dl}{dw_1}=2(x_1w_1+x_2w_2-y)x_1$$
$$\frac{dl}{dw_1}=2(x_1w_1+x_2w_2-y)x_1$$

Когда $x_1$ и $x_2$ будут иметь сильно разный масштаб, градиенты по параметрам тоже будут иметь сильно разный масштаб. И это именно то, что будет ломать градиентный спуск.

Далее разберём функцию, которая будет рисовать градиентный спуск, и так же поэкспериментируем с линиями уровня.

# 4. Batch нормализация

После инициализации и запуска back-propagation нет гарантий, что дисперсия не будет расти. Для нормирования выходов нейронов (до и после активации) можно использовать Batch нормализацию.

Batch нормализация пытается нормировать каждый выход нейрона таким образом, чтобы у него были нулевое среднее и фиксированная дисперсия.

Экспоненциальное сглаживание работает следующим образом: когда мы получаем среднее по батчу и Var по батчу, мы добавляем их в накопитель с некоторым весом, а старое значение в накопителе немного дискаунтируем.

## Что делать с $\gamma$ и $\beta$?

$\gamma$ и $\beta$ нужны для масштабирования и сдвига активации — нейросети может быть полезно иметь, например,  не единичную дисперсию для какого-то нейрона, а большую, что поможет ей сойтись лучше.

Линейная комбинация каких-то других входов легко дифференцируется, поэтому эти коэффициенты можно добавить в  back-propagation, по ним будут считаться градиенты, и они будут автоматически подобраны.

# 5. Dropout регуляризация

Dropout регуляризация на каждом шаге back-propagation семплирует сеть и с вероятностью $p$ оставляет каждый нейрон, но с вероятность $1-p$ заменяет его на 0. Таким образом сеть подстраивается по частям.

<center><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block@DSLIGHT_DL_4_5_1.png" style="width: 800px;">
</center>

## Дополнительные материалы

[Dropout: A Simple Way to Prevent Neural Networks from Overfitting](http://www.cs.toronto.edu/~rsalakhu/papers/srivastava14a.pdf)


# 6. Производная функции

В зависимости от того, какую величину шага в градиентном спуске learning rate вы выберете (большую или маленькую), вариации градиентного спуска будут выглядеть по-разному:

<ul class="list">
<li>Если learning rate <b>слишком большой</b>, это означает, что сначала оптимизация была, но остановилась и качество становится хуже,&nbsp;<b>мы выходим из оптимальной точки</b>.</li>
<li>Если learning rate <b>слишком маленький</b>, то <b>обучение </b>слишком <b>медленное</b>.</li>
<li>Если learning rate <b>недостаточно большой</b>, то поначалу обучение идёт отлично, а потом мы <b>застреваем и не двигаемся дальше</b>.</li>
<li>Если learning rate <b>оптимальный</b>, то мы <b>обучаемся быстро вначале и к концу мы выходим на оптимальную точку</b>.</li>
</ul>

<p style="text-align: center;"><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block@DSLIGHT_DL_4_6_1.png" style="width: 800px;"></p>

<div class="color-container container-flex blue-container">
<div class="container-icon"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 26 26" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M6.99581 3.99658C6.99581 6.20664 5.2042 7.99825 2.99414 7.99825C5.2042 7.99825 6.99581 9.78986 6.99581 11.9999C6.99581 9.78986 8.78741 7.99825 10.9975 7.99825C8.78741 7.99825 6.99581 6.20664 6.99581 3.99658Z" stroke="red" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path fill-rule="evenodd" clip-rule="evenodd" d="M18.0021 16.0017C18.0021 13.2392 15.7626 10.9996 13 10.9996C15.7626 10.9996 18.0021 8.76013 18.0021 5.99756C18.0021 8.76013 20.2416 10.9996 23.0042 10.9996C20.2416 10.9996 18.0021 13.2392 18.0021 16.0017Z" stroke="red" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path fill-rule="evenodd" clip-rule="evenodd" d="M10.9978 14.501C10.9978 16.711 9.20615 18.5026 6.99609 18.5026C9.20615 18.5026 10.9978 20.2942 10.9978 22.5043C10.9978 20.2942 12.7894 18.5026 14.9994 18.5026C12.7894 18.5026 10.9978 16.711 10.9978 14.501Z" stroke="red" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </svg></div>
<span><strong>Почему стоит снижать learning rate с каждой итерацией?</strong><br><br><i> Если уменьшить learning rate, когда вы увидели, что обучение больше не происходит, то сеть еще чуть-чуть доучится.</i> </span></div>
<p></p>
Проблема градиентного спуска — он застревает в локальных минимумах.

<p style="text-align: center;"><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block@DSLIGHT_DL_4_6_2.png" style="width: 400px;"></p>

## Дополнительные материалы

<div class="color-container container-flex orange-container">
<div class="container-icon"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 26 26" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M12.9998 17.8658C10.971 15.8359 7.91272 15.4628 5.50472 16.7463C4.82144 17.1105 3.99609 16.6613 3.99609 15.887V6.79116C3.99609 6.1549 4.29022 5.54264 4.80843 5.17349C7.29447 3.40075 10.7689 3.62985 12.9998 5.86078C15.2308 3.62985 18.7052 3.40075 21.1913 5.17349C21.7095 5.54264 22.0036 6.1549 22.0036 6.79116V15.887C22.0036 16.6613 21.1782 17.1115 20.495 16.7463C18.087 15.4628 15.0287 15.8359 12.9998 17.8658Z" stroke="green" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M5.50391 20.8845C7.91191 19.601 10.9702 19.9741 12.999 22.004C15.0279 19.9741 18.0861 19.601 20.4941 20.8845" stroke="green" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M13.0002 17.8663V5.86133" stroke="green" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </svg></div>
<ul class="list">
<li><a href="https://wiseodd.github.io/techblog/2016/06/22/nn-optimization/" target="_blank" rel="noopener">Beyond SGD: Gradient Descent with Momentum and Adaptive Learning Rate</a></li>
<li><a href="https://hackernoon.com/life-is-gradient-descent-880c60ac1be8" target="_blank" rel="noopener">Life is gradient descent</a></li>
</ul>
</div>

# 7. Стохастический градиентный спуск (SGD)


<div class="term"><b><span>Стохастический градиентный спуск</span></b><span> <b>(SGD) </b>&nbsp;является итерационным методом оптимизации с дифференцируемой целевой функцией, суть градиентного спуска — минимизировать функцию, делая небольшие шаги в сторону наискорейшего убывания функции.</span></div>
<p></p>
<p>Плюсы SGD:<span><o:p></o:p></span></p>
<ul class="list">
<li>позволяет быстрее делать шаги и быстрее сходиться;</li>
<li>траектория становится более шумной, что помогает выпрыгивать из локальных оптимумов.</li>
</ul>
<div class="term"><b><span>RMSProp</span></b>&nbsp;—&nbsp;адаптивный шаг.&nbsp;RMSProp<span> — метод, в котором скорость обучения адаптируется для каждого из параметров.</span></div>
<p><span>Градиентные методы медленно сходятся, если градиенты по разным параметрам в разном масштабе. К</span><span>ак их привести в один масштаб? Если мы делали несколько маленьких шагов по какой-то переменной, то можно увеличивать шаг, чтобы не делать оптимизацию слишком медленной по некоторым переменным. Т.е. мы делим скорость обучения для веса на скользящее среднее значение после градиентов для этого веса.</span><span><o:p></o:p></span></p>
<div class="term"><strong><span>Adam</span></strong>&nbsp;—&nbsp;<span style="font-size: 1em;">Adaptive Moment Estimation.&nbsp;</span>Adam<span>&nbsp;</span>—&nbsp;<span style="font-size: 1em;">метод, в котором сочетаются инерция и адаптивность шага.&nbsp;</span>Если перед вами стоит выбор вариации SGD, то выбирайте Adam.</div>
<h3>Дополнительные материалы</h3>
<div class="color-container container-flex orange-container">
<div class="container-icon"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 26 26" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M12.9998 17.8658C10.971 15.8359 7.91272 15.4628 5.50472 16.7463C4.82144 17.1105 3.99609 16.6613 3.99609 15.887V6.79116C3.99609 6.1549 4.29022 5.54264 4.80843 5.17349C7.29447 3.40075 10.7689 3.62985 12.9998 5.86078C15.2308 3.62985 18.7052 3.40075 21.1913 5.17349C21.7095 5.54264 22.0036 6.1549 22.0036 6.79116V15.887C22.0036 16.6613 21.1782 17.1115 20.495 16.7463C18.087 15.4628 15.0287 15.8359 12.9998 17.8658Z" stroke="green" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M5.50391 20.8845C7.91191 19.601 10.9702 19.9741 12.999 22.004C15.0279 19.9741 18.0861 19.601 20.4941 20.8845" stroke="green" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M13.0002 17.8663V5.86133" stroke="green" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </svg></div>
<ul class="list">
<li><a href="https://distill.pub/2017/momentum/" target="_blank" rel="noopener">Why Momentum Really Works</a></li>
<li><a href="http://ruder.io/optimizing-gradient-descent/" target="_blank" rel="noopener">An overview of gradient descent optimization algorithms</a></li>
</ul>
</div>
</div>

# 8. Adam - Adaptive Moment Estimation

<a href="file:///home/denis/Документы/Cource_on_DS/IDE/learning/Deep_learning_in_Data_Sciences/skillfactory_dl_4_screencast.ipynb">Перейти на ноутбук к скринкасту</a>

В предыдущей задаче оптимизации MSE мы остановились на том, что при увеличении learning rate, возникает осциллирование траектории.

Теперь мы рассмотрим на практике Adam. Запустим его на задаче, в которой признаки (а значит, и градиент) приблизительно одинакового масштаба. 

<p style="text-align: center;"><img width="60%" src="https://lms-cdn.skillfactory.ru/assets/courseware/v1/ea49ce24260b133bb0d5584be86aa53a/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/MAT_3_unit_06.jpg" alt="рис"></p>

Сплющив вертикальную ось, заметим, что линии уровня станут сплюснутыми, а Adam сходится всё так же быстро.

```python
# узкие долины функции
plot_gd(x_scale=0.5, lr=0.1, steps=25, optimizer='adam')
```

Всё дело в адаптивном шаге, что нормирует градиенты и позволяет оптимально двигаться во всех направлениях.

Задавая ещё более узкие долины, убедимся в этом.

Теперь увеличим learning rate в 20 раз.

<p style="text-align: center;"><img width="60%" src="https://lms-cdn.skillfactory.ru/assets/courseware/v1/f8268b5bb35913f197d0264d8e99dc14/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/MAT_3_unit_07.jpg" alt="рис"></p>

Но тем не менее в итоге мы сошлись к самому хорошему решению.

Learning rate — это гиперпараметр, который нужно подбирать, и всё, конечно, зависит от того, как выглядит форма Loss-функции.

# 9. Матричные операции

## Интерфейс прямого прохода

Для прямого прохода интерфейс очень простой — это функция, которая принимает вход и генерирует выход, т.е. один вход и один выход.

Обратный проход производится по графу из производных, т.е. когда мы идем по нему в обратную сторону, мы рассчитываем с помощью цепного правила производные по всем параметрам, которые есть в сети.

Чтобы реализовать Backward pass для новой вершины нужно реализовать функцию, у которой есть входы —  то, что использовалось как вход сигмоиды во время прямого прохода. Т.к. необходимо считать производную в какой-то точке, сначала  back-propagation делает прямой проход, запоминает все значения аргументов, а потом использует их во время обратного прохода, чтобы рассчитать производные функций в нужных точках.

<p style="text-align: center;"><img width="80%" src="https://lms-cdn.skillfactory.ru/assets/courseware/v1/aaefb63b856f2602eb80cf9c1682bfe3/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DSLIGHT_DL_4_10_1.png" alt="рис"></p>

## Полносвязный слой как произведение матриц

Матричные операции используются часто, они реализованы быстро. Существуют такие пакеты как: CPU (BLAS) и GPU (cuBLAS), которые производят численные операции очень быстро, используя векторные операции процессора.

## Быстрая реализация в NumPy

Производит матричные операции очень быстро, не на Python, и NumPy можно настроить таким образом, чтобы он использовал те же инструкции, что заложены в пакетах BLAS.