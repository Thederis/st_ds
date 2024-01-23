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
<div class="container-icon"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 26 26" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M12.9998 17.8658C10.971 15.8359 7.91272 15.4628 5.50472 16.7463C4.82144 17.1105 3.99609 16.6613 3.99609 15.887V6.79116C3.99609 6.1549 4.29022 5.54264 4.80843 5.17349C7.29447 3.40075 10.7689 3.62985 12.9998 5.86078C15.2308 3.62985 18.7052 3.40075 21.1913 5.17349C21.7095 5.54264 22.0036 6.1549 22.0036 6.79116V15.887C22.0036 16.6613 21.1782 17.1115 20.495 16.7463C18.087 15.4628 15.0287 15.8359 12.9998 17.8658Z" stroke="#FFF0EC" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M5.50391 20.8845C7.91191 19.601 10.9702 19.9741 12.999 22.004C15.0279 19.9741 18.0861 19.601 20.4941 20.8845" stroke="#FFF0EC" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M13.0002 17.8663V5.86133" stroke="#FFF0EC" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </svg></div>
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
<div class="container-icon"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 26 26" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M12.9998 17.8658C10.971 15.8359 7.91272 15.4628 5.50472 16.7463C4.82144 17.1105 3.99609 16.6613 3.99609 15.887V6.79116C3.99609 6.1549 4.29022 5.54264 4.80843 5.17349C7.29447 3.40075 10.7689 3.62985 12.9998 5.86078C15.2308 3.62985 18.7052 3.40075 21.1913 5.17349C21.7095 5.54264 22.0036 6.1549 22.0036 6.79116V15.887C22.0036 16.6613 21.1782 17.1115 20.495 16.7463C18.087 15.4628 15.0287 15.8359 12.9998 17.8658Z" stroke="blue" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M5.50391 20.8845C7.91191 19.601 10.9702 19.9741 12.999 22.004C15.0279 19.9741 18.0861 19.601 20.4941 20.8845" stroke="blue" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M13.0002 17.8663V5.86133" stroke="blue" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </svg></div>
<ul class="list">
<li><a href="https://slideplayer.com/slide/7341917/" target="_blank" rel="noopener">Computacion Inteligente Derivative-Based Optimization</a></li>
<li><a href="https://en.wikipedia.org/wiki/Variance" target="_blank" rel="noopener">Sum of uncorrelated variables (Bienaymé formula)</a></li>
<li><a href="http://proceedings.mlr.press/v9/glorot10a/glorot10a.pdf" target="_blank" rel="noopener">Understanding the difficulty of training deep feedforward neural networks</a></li>
</ul>
</div>
</div>