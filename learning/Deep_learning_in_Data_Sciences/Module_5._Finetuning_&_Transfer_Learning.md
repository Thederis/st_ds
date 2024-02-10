# 1/17   1. Введение

<div class="main-block">
<p>В этом модуле речь пойдёт о <strong>переносе обучения</strong> или&nbsp;<strong>Transfer learning</strong>.</p>
<p>Обучение нейронной сети требует большого объёма данных, например, в ImageNet это миллионы картинок. Что делать, если в текущей задаче не так много данных?</p>
<p>Оказывается, в решении новой задачи можно переиспользовать часть нейросети, которая училась на ImageNet*.</p>
<p class="grey-text">* <strong>ImageNet</strong> — база данных аннотированных изображений, предназначенная для отработки и тестирования методов распознавания образов и машинного зрения. ImageNet использует краудсорсинг для аннотирования изображений. ImageNet — это dataset, организованный в соответствии с иерархией WordNet.</p>
<p>Сеть, которая обучилась на&nbsp;ImageNet, рассматривают, как состоящую из:</p>
<ul class="list">
<li>первая часть (на рисунке синяя) состоит из <strong>конволюционных слоёв</strong> и извлекает из картинки признаки;</li>
<li>вторая часть (на рисунке оранжевая) с помощью <strong>многослойного персептрона (MLP)</strong> по признакам определяет, к какому из тысячи классов принадлежит картинка.</li>
</ul>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/2715587cc14f6ef255902a2a02e5234d/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_1_1.png" style="width: 630px;"></p>
<p>Первую (синюю) часть такой сети можно переиспользовать в новой задаче. Такой подход называется переносом обучения или Transfer learning. Таким образом, чтобы обучить сеть на новой задаче, необходимо доучить только крайний полносвязный слой.</p>
<p>Нейроны на разных слоях сети, которую учили на ImageNet, реагируют по-разному:</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/3c10a7700a7df1157e47447b94f4675d/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_2.png" style="width: 800px;"></p>
<h3>Дополнительные материалы</h3>
<div class="color-container container-flex orange-container">
<div class="container-icon"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 26 26" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M12.9998 17.8658C10.971 15.8359 7.91272 15.4628 5.50472 16.7463C4.82144 17.1105 3.99609 16.6613 3.99609 15.887V6.79116C3.99609 6.1549 4.29022 5.54264 4.80843 5.17349C7.29447 3.40075 10.7689 3.62985 12.9998 5.86078C15.2308 3.62985 18.7052 3.40075 21.1913 5.17349C21.7095 5.54264 22.0036 6.1549 22.0036 6.79116V15.887C22.0036 16.6613 21.1782 17.1115 20.495 16.7463C18.087 15.4628 15.0287 15.8359 12.9998 17.8658Z" stroke="#FF0FFF" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M5.50391 20.8845C7.91191 19.601 10.9702 19.9741 12.999 22.004C15.0279 19.9741 18.0861 19.601 20.4941 20.8845" stroke="#FF0FFF" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M13.0002 17.8663V5.86133" stroke="#FF0FFF" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </svg></div>
<ul class="list">
<li><a href="https://distill.pub/2017/feature-visualization/" target="_blank" rel="noopener">Feature Visualization. How neural networks build up their understanding of images</a></li>
<li><a href="https://www.youtube.com/watch?v=c7d2E_zkju8&amp;feature=youtu.be" target="_blank" rel="noopener">AvitoNet: сервис компьютерного зрения в Avito</a></li>
</ul>
</div>
</div>

# 2. Как получить такие картинки

<div class="main-block">
<p>Как получить картинки, которые рисуют, на что реагируют нейроны?</p>
<p>Нейронная сеть дифференцируема,&nbsp;каждый нейрон&nbsp;является сложной функцией.&nbsp;Достаточно подобрать вход, который даст максимальную активацию на отдельно взятый нейрон. Аргументами функции, которые подбираются с помощью обратного распространения ошибки, является входное изображение. Фактически&nbsp;организуется&nbsp;статистический градиентный спуск, в ходе которого изображение приобретает осмысленный вид.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/f308d77db72f4d6609970be2bf61f4fb/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_3.png" style="width: 800px;"></p>
<p>Строить такие картинки можно, используя целый слой или канал в слое.&nbsp;Задача: найти, на что среагирует нейрон,&nbsp;при помощи<strong> метода градиентного спуска</strong> (SGD).</p>
<p>Если взять на картинке один нейрон, то картинка, которая будет подобрана при помощи SGD, будет содержать кусочек текстуры только в той части изображения, на которую смотрит этот нейрон. Каждый нейрон имеет ограниченное поле обзора. «Слепых пятен» можно избежать, взяв все нейроны слоя.&nbsp;</p>
<p>Можно максимизировать выход одного нейрона, канала,&nbsp;слоя или целого выхода сети для конкретного класса.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/0e0ef5c2a7db67ab769a88a41a5d9eb6/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_4.png" style="width: 800px;"></p>
<p>Также можно взять выход нейронной сети, который соответствует конкретному классу, и под него подбирать изображение при помощи SGD.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/5a748b96a65ad7101abcd79a8d9a91ca/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_6.png" style="width: 800px;"></p>
<p>Другой способ: в dataset, используемом при обучении, взять картинки, на которых конкретный <strong>нейрон даёт максимальную активацию</strong>.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/da64bf36b24163f8feed60cf0cb8d88d/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_5.png" style="width: 800px;"></p>
<p>В этом случае нужно намного меньше данных для обучения последних слоёв.</p>
<p>Перенос обучения работает, если новая задача похожа на ImageNet (содержит те же объекты или похожие). Стоит также учесть, что в ImageNet нет лиц.</p>
</div>

# 3. Перенос обучения

<div class="main-block">
<p>Разберём задачу распознавания эмоций по фотографии. Если бы нейронная сеть обучалась нами с нуля, то экстрактор выглядел бы следующим образом</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/0cfbbccf0402adbf58de873b1dc4da5b/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_7.png" style="width: 570px;"></p>
<p>В ImageNet сети, наверняка, уже есть детекторы краёв&nbsp;и простые текстуры, которые можно использовать в нашей задаче. Остальные текстуры необходимо будет выучить, используя дополнительные данные для дообучения сети.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/57eb8d0f6e1e6e2562061c2962212104/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_8.png" style="width: 570px;"></p>
<p>Взяв первые несколько слоёв из&nbsp;фича-экстрактора, который обучен по&nbsp;ImageNet, останется дообучить только последние слои нейронной сети.</p>
</div>

# 4. Fine-tuning

<div class="main-block">
<p>Рассмотрим сеть, которая обучена на&nbsp;ImageNet.&nbsp;Фиксируем в этой сети часть фича-экстрактора (зелёная на рисунке).</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/1832924a1ad3c7541a148cf8e972452a/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_9.png" style="width: 580px;"></p>
<p>Тогда в новой задаче дообучить предстоит только синий и тёмно-зелёный слои.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/626ab1f6165cf83867a8d90d1a0e7c1a/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_10.png" style="width: 580px;"></p>
<p>Здесь используется <strong>fine-tuning </strong>—&nbsp;<span style="font-size: 1em;">связный приём, очень похожий на transfer learning. Заключается он в следующем:</span></p>
<p><span style="font-size: 1em;">Синие свёрточные слои будем инициализировать не случайными значениями, а теми же, что использовались в ImageNet сети. Тёмно-зелёный слой зафиксируем, а синий слой инициализируем теми же весами, которые получили от ImageNet сети. И пустим градиенты с маленьким шагом, чтобы подстроить слои под нашу задачу.</span></p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/0e8a094ccba91f5a7add1ce07458baee/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_11.png" style="width: 580px;"></p>
<p style="text-align: center;"></p>
<h3>Преимущества fine-tuning</h3>
<p>Fine-tuning — это очень популярный подход, т.к.<strong></strong></p>
<ul class="list">
<li>ImageNet покрывает огромное количество объектов, которые есть в реальном мире.</li>
<li>В Keras есть веса для обученных на ImageNet VGG, Inception, ResNet и т.д.</li>
<li>Можно легко сделать ансамбль из этих сетей.</li>
</ul>
<p>Резюмируя, обратимся к следующей таблице:</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/62e7fe5a6a6d57172a78f08f7271f615/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_12.png" style="width: 580px;"></p>
<h3>Дополнительные материалы</h3>
<div class="color-container container-flex orange-container">
<div class="container-icon"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 26 26" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M12.9998 17.8658C10.971 15.8359 7.91272 15.4628 5.50472 16.7463C4.82144 17.1105 3.99609 16.6613 3.99609 15.887V6.79116C3.99609 6.1549 4.29022 5.54264 4.80843 5.17349C7.29447 3.40075 10.7689 3.62985 12.9998 5.86078C15.2308 3.62985 18.7052 3.40075 21.1913 5.17349C21.7095 5.54264 22.0036 6.1549 22.0036 6.79116V15.887C22.0036 16.6613 21.1782 17.1115 20.495 16.7463C18.087 15.4628 15.0287 15.8359 12.9998 17.8658Z" stroke="#FFF0EC" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M5.50391 20.8845C7.91191 19.601 10.9702 19.9741 12.999 22.004C15.0279 19.9741 18.0861 19.601 20.4941 20.8845" stroke="#FFF0EC" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M13.0002 17.8663V5.86133" stroke="#FFF0EC" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </svg></div>
<span><a href="https://flyyufelix.github.io/2016/10/03/fine-tuning-in-keras-part1.html" target="_blank" rel="noopener">A Comprehensive guide to Fine-tuning Deep Learning Models in Keras (Part I)</a></span></div>
</div>

# 5. Автокодировщики

<div class="main-block">
<div class="term"><strong>Автокодировщики</strong> (autoencoders) — это специальная архитектура нейронной сети, позволяющая сжимать входные данные.&nbsp;Автокодировщик сжимает входные признаки в более компактное представление, которое не теряет информации об исходных данных.</div>
<p>Encoder сжимает признаковое описание на входе, decoder расшифровывает эту информацию обратно, не изменяя входные данные:</p>
<ul class="list">
<li>Encoder = data to hidden</li>
<li>Decoder = hidden to data</li>
<li>Decoder(Encoder(x)) ~ x (близость по MSE)</li>
</ul>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/89c36578717e43afd768667f2c8d6e94/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_13.png" style="width: 600px;"></p>
<p>Такое сжатое представление или <strong>bottleneck</strong>&nbsp;(горлышко бутылки) будет полезным для решения задач.</p>
<h2>Вспомним про PCA (метод главных компонент)</h2>
<p>Данный метод основан на представлении исходной матрицы признаков в виде произведения других матриц и позволяет найти пространство меньшей размерности, хорошо описывающее входные данные. Этот метод в следующем модуле будет разобран подробно.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/540f9d625d9a3bbbfb4d92cdc69a13e5/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_14.png" style="width: 600px;"></p>
<p>Такую задачу можно переписать в виде нейронной сети:</p>
<table style="width: 99.9854%;">
<tbody>
<tr>
<td style="border: none; vertical-align: middle; width: 51.9631%;">
<p><strong>D признаков</strong> на входе при помощи полносвязного слоя <strong>Encoder</strong> сжимаем до представления в <strong>H признаков</strong>.</p>
<p>H много меньше D.</p>
<p>Полносвязный<strong> слой Decoder</strong> с помощью маленького представления H пытается восстановить исходные D признаков.</p>
<p><strong>Цель</strong> обучения такой нейросети в том, чтобы представление H, пропущенное через сеть, не изменяло входные данные.</p>
</td>
<td style="border: none; vertical-align: middle; width: 48.0223%;" width="50%"><img width="100%" src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/f220660b107b879e59eca47b1f156ba0/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_15.png"></td>
</tr>
</tbody>
</table>
<p>Метод главных компонент позволяет сжимать картинку в 10 раз.</p>
</div>

# 6. Un-pooling

<div class="main-block">
<p>Результат предыдущего метода можно улучшить. Ведь для изображений применяются свёрточные нейронные сети.</p>
<p>Добавим свёрточные слои.</p>
<p>К исходной картинке применим свёрточный слой, описывая каждый пиксель изображения по пикселям, которые были в окрестности исходного изображения. Добавим ещё несколько слоёв.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/affe00c658d66f42775e0d3492fdac80/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_16.png" style="width: 550px;"></p>
<p>На выходе предстоит&nbsp;«схлопнуть» представление в картинку исходного расширения с одним или тремя (в случае цветного изображения) выходными каналами. При помощи среднеквадратичных потерей можно обучить это преобразование.&nbsp;Но это достаточно наивный подход, т.к. требует&nbsp;слишком много вычислений и не содержит «bottleneck».</p>
<p>Чтобы получить компактное представление в таких сетях, добавим&nbsp;<strong>pooling слой</strong>.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/2163a299c1fbbfc8328f79f88cd4b0ce/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_17.png" style="width: 350px;"></p>
<p>Pooling слой будет сжимать изображение в два раза. На выходе получим небольшой тензор, который можно вытянуть в вектор,&nbsp;— это и будет представлением для картинки. Это представление будем называть <b>embedding&nbsp;</b>или результатом encoder.</p>
<p>Как развернуть полученный вектор из числа обратно в картинку? Кажется естественным повторить преобразование encoder&nbsp;в обратную сторону.&nbsp;Как обратить результат pooling слоя? Используем&nbsp;un-pooling слой.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/57bf29a92c2112c74ab0f3837e3b7dd9/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_18.png" style="width: 480px;"></p>
<h2>Un-pooling</h2>
<p>Рассмотрим простой вариант. Будем делать un-pooling&nbsp;при помощи заполнения ячеек теми же значениями, которые были рядом, интерполируя значения ближайшего соседа.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/0100fd27d2c0e7c8e17bc0f8c2089c4c/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_19.png" style="width: 400px;"></p>
<p>Такой простой подход работает. Свёрточные слои после&nbsp;un-pooling сгладят&nbsp;«плохие» преобразования. Всю эту сеть можно обучить при помощи средней квадратичной ошибки MSE.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/48c980b8d3a7e7b0e5d526bdb07ffdea/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_20.png" style="width: 800px;"></p>
</div>

# 7. Поиск похожих изображений

<div class="main-block">
<p>Пусть нам нужно сравнить два изображения.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/953a1c114b87687dd80156a231c2b8a8/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_21.png" style="width: 580px;"></p>
<p>Понятно, что на картинках может быть один и тот же объект, но с разных ракурсов. Сравнивать попиксельно невозможно, необходимы признаки более высокого уровня, которые может дать конволюционная сеть.&nbsp;</p>
<p>Возьмём большое количество таких лиц и прогоним через autoencoder.&nbsp;Результат работы encoder&nbsp;(bottleneck) для каждого изображения запомним, как вектор. Поиск похожих изображений будет заключаться в поиске похожих векторов. И это работает!</p>
<p><strong>Denoising autoencoders</strong>&nbsp;— ещё одно применение&nbsp;autoencoders.&nbsp;Denoising autoencoders учатся удалять шум с изображения.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/78e3032d6d6f94e9ce3f0b36d269b362/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_22.png" style="width: 580px;"></p>
</div>

# 8. Быстрый KNN

Метод <strong>aproximent k-nearest neighbors</strong> позволяет приблизительно найти $k$ ближайших соседей.
<p><a title="Ссылка на GitHub" href="https://github.com/erikbern/ann-benchmarks" target="_blank" rel="noopener">Методы</a>, работающие по этому принципу, устроены более или менее одинаково.&nbsp; Они пытаются специальным образом проиндексировать пространство&nbsp;embedding, чтобы в нём можно было быстро искать вектор, который наиболее похож на заданный.</p>
<p>Например, на задачах <strong>Fashion MNIST</strong>&nbsp;можно взять вектор, который получается из нашей нейронной сети, и по нему искать ближайшие картинки. На представленном графике по горизонтальной оси отложена полнота поиска, по вертикальной — сколько запросов в секунду мы можем выполнять для такого поиска.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/d69a97e8e8b67b1644b61764bc51b9cd/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_23.png" style="width: 800px;"></p>
<h2>Полнота поиска</h2>
<p>Пусть&nbsp;по выбранной картинке честно найдены 100 штук наиболее похожих на&nbsp;неё. Приближённым способом также ищем 100 наиболее похожих на нашу картинку.&nbsp;</p>
<p>Если в сотне приближённо найденных картинок найдётся 95 из сотни реально похожих, будем говорить, что полнота 95 %. В этом случае можно сказать, что приближённый метод отработал хорошо.</p>
<p>Самые продвинутые методы основаны на&nbsp;<strong>hnsw</strong>&nbsp;и дают 10 000 запросов в секунду при полноте в 95 %.<em></em></p>
<h3>Дополнительные материалы</h3>
<div class="color-container container-flex orange-container">
<div class="container-icon"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 26 26" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M12.9998 17.8658C10.971 15.8359 7.91272 15.4628 5.50472 16.7463C4.82144 17.1105 3.99609 16.6613 3.99609 15.887V6.79116C3.99609 6.1549 4.29022 5.54264 4.80843 5.17349C7.29447 3.40075 10.7689 3.62985 12.9998 5.86078C15.2308 3.62985 18.7052 3.40075 21.1913 5.17349C21.7095 5.54264 22.0036 6.1549 22.0036 6.79116V15.887C22.0036 16.6613 21.1782 17.1115 20.495 16.7463C18.087 15.4628 15.0287 15.8359 12.9998 17.8658Z" stroke="#C000CC" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M5.50391 20.8845C7.91191 19.601 10.9702 19.9741 12.999 22.004C15.0279 19.9741 18.0861 19.601 20.4941 20.8845" stroke="#C000CC" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M13.0002 17.8663V5.86133" stroke="#C000CC" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </svg></div>
<ul class="list">
<li><a href="https://github.com/erikbern/ann-benchmarks" target="_blank" rel="noopener">Benchmarking nearest neighbors</a></li>
<li><a href="https://github.com/ikibardin/kaggle-camera-model-identification" target="_blank" rel="noopener">Code for reproducing 2nd place solution for Kaggle competition IEEE's Signal Processing Society</a></li>
</ul>
</div>

# 9. Пространство представлений

<div class="main-block">
<p>Рассмотрим на примере, как работает поиск похожих изображений.</p>
<p>Возьмём картинку, на которой человек улыбается, превратим её в вектор и найдём ближайшие картинки по близости векторов. Окажется, что на ближайших картинках изображены лица людей, которые&nbsp;имеют схожий ракурс и улыбку.</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/8e3cc60683327a37f830930c7dc00aa1/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_24.png" style="width: 550px;"></p>
<p>Другой пример: для не улыбающегося лица в очках найдутся следующие похожие картинки:</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/53478e19f3251d639b43da075b33a95d/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_25.png" style="width: 550px;"></p>
<p>В пространстве&nbsp;embedding мы можем делать интерполяцию, плавно меняя картинку</p>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/9fbb6de35a1bd0cc6ff5aa6df4a39fb6/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_26.png" style="width: 750px;"></p>
</div>

# 10. Вывод

<div class="main-block">
<div style="position: relative; padding-top: 56.25%; width: 100%; margin-bottom: 50px;"><iframe style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border-radius: 8px;" src="https://kinescope.io/embed/200939413?externalid=111132" allow="autoplay; fullscreen; picture-in-picture; encrypted-media;" frameborder="0" allowfullscreen="allowfullscreen"></iframe></div>
<p>Для чего нужны <i>autoencoder</i>?</p>
<ul class="list-unstyled">
<li>Нам не нужны размеченные данные! Учим экстрактор признаков за бесплатно!</li>
<li>Полученный экстрактор можно файн-тьюнить под нашу задачу!</li>
</ul>
<p style="text-align: center;"><img src="http://lms-cdn.skillfactory.ru/assets/courseware/v1/0da151704d0e580d9c51e7cec5d989c7/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/DL-2_5_%D0%BC%D0%BE%D0%B4%D1%83%D0%BB%D1%8C_27.png" style="width: 500px;"></p>
<p>В этом модуле мы рассмотрели два важных подхода к нейросетевым представлениям:</p>
<ol class="ordered-list">
<li><strong>Finetuning / Transfer learning</strong>, в котором смотрим на часть нейросети, как на экстрактор признаков для нашей задачи, который можем полностью или частично переиспользовать.</li>
<li>Второй подход заключается в использовании&nbsp;неразмеченных данных, где учим&nbsp;autoencoder и его encoder-часть берём как экстрактор признаков.</li>
</ol>
</div>

# 11. Практика. Часть 1-5


<div class="main-block">
<p><a href="https://www.kaggle.com/itslek/transfer-learning-keras-flowers-sf-dl-v1?scriptVersionId=31741245" target="_blank" rel="noopener">Ноутбук к скринкасту</a></p>
<div class="color-container container-flex blue-container">
<div class="container-icon"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 26 26" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M6.99581 3.99658C6.99581 6.20664 5.2042 7.99825 2.99414 7.99825C5.2042 7.99825 6.99581 9.78986 6.99581 11.9999C6.99581 9.78986 8.78741 7.99825 10.9975 7.99825C8.78741 7.99825 6.99581 6.20664 6.99581 3.99658Z" stroke="#F00CCC" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path fill-rule="evenodd" clip-rule="evenodd" d="M18.0021 16.0017C18.0021 13.2392 15.7626 10.9996 13 10.9996C15.7626 10.9996 18.0021 8.76013 18.0021 5.99756C18.0021 8.76013 20.2416 10.9996 23.0042 10.9996C20.2416 10.9996 18.0021 13.2392 18.0021 16.0017Z" stroke="#EEE00E" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path fill-rule="evenodd" clip-rule="evenodd" d="M10.9978 14.501C10.9978 16.711 9.20615 18.5026 6.99609 18.5026C9.20615 18.5026 10.9978 20.2942 10.9978 22.5043C10.9978 20.2942 12.7894 18.5026 14.9994 18.5026C12.7894 18.5026 10.9978 16.711 10.9978 14.501Z" stroke="#CCCCCC" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </svg></div>
<span><strong>Важно!</strong> Обратите внимание, что ноутбуки данного модуля актуальны для версии tensorflow 2.1, поэтому их нельзя запустить в Google Colab. Для работы с ними воспользуйтесь исполняемой средой kaggle.</span></div>
</div>

<h3>Полезные ссылки</h3>
<div class="color-container container-flex orange-container">
<div class="container-icon"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 26 26" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M12.9998 17.8658C10.971 15.8359 7.91272 15.4628 5.50472 16.7463C4.82144 17.1105 3.99609 16.6613 3.99609 15.887V6.79116C3.99609 6.1549 4.29022 5.54264 4.80843 5.17349C7.29447 3.40075 10.7689 3.62985 12.9998 5.86078C15.2308 3.62985 18.7052 3.40075 21.1913 5.17349C21.7095 5.54264 22.0036 6.1549 22.0036 6.79116V15.887C22.0036 16.6613 21.1782 17.1115 20.495 16.7463C18.087 15.4628 15.0287 15.8359 12.9998 17.8658Z" stroke="#FF0000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M5.50391 20.8845C7.91191 19.601 10.9702 19.9741 12.999 22.004C15.0279 19.9741 18.0861 19.601 20.4941 20.8845" stroke="#FF0000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path d="M13.0002 17.8663V5.86133" stroke="#FF0000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </svg></div>
<span><a href="https://paperswithcode.com/sota" target="_blank" rel="noopener">Paperswithcode</a><br><br><a href="https://sotabench.com/benchmarks/image-classification-on-imagenet" target="_blank" rel="noopener">Sotabench</a><br><br><a href="https://github.com/qubvel/efficientnet" target="_blank" rel="noopener">efficientnet на GitHub</a></span></div>
</div>
<p></p>

[Перейти к файлу в системе(относительный путь)](./fine_tuning_flowers_solved.ipynb)
<p></p>

# 16. Дополнительно

## Как работать с Kaggle Kernels
[Скачать ноутбук к скринкасту](https://lms-cdn.skillfactory.ru/assets/courseware/v1/84ebc92facec17c77190355ad89b4f0e/asset-v1:SkillFactory+MFTIDSLIGHT+2022_DEC+type@asset+block/fine_tuning_flowers_solved.ipynb)

Ссылка на видео в системе:
![Video](../../../../../../../home/denis/Документы/Cource_on_DS/Screenrecorder-2024-02-05-17-17-49-165.mp4)

