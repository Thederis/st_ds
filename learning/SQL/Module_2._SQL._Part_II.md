# 1. Основные агрегатные функции
<div class="main-block">
<p>Как и большинство других серверов реляционных баз данных, Postgres, которая используется в этом тренажёре, поддерживает <strong>агрегатные функции</strong>. Что это такое?</p>
<div class="color-container container-flex blue-container">
<div class="container-icon"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 26 26" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M6.99581 3.99658C6.99581 6.20664 5.2042 7.99825 2.99414 7.99825C5.2042 7.99825 6.99581 9.78986 6.99581 11.9999C6.99581 9.78986 8.78741 7.99825 10.9975 7.99825C8.78741 7.99825 6.99581 6.20664 6.99581 3.99658Z" stroke="#D1D0FD" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path fill-rule="evenodd" clip-rule="evenodd" d="M18.0021 16.0017C18.0021 13.2392 15.7626 10.9996 13 10.9996C15.7626 10.9996 18.0021 8.76013 18.0021 5.99756C18.0021 8.76013 20.2416 10.9996 23.0042 10.9996C20.2416 10.9996 18.0021 13.2392 18.0021 16.0017Z" stroke="#D1D0FD" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path fill-rule="evenodd" clip-rule="evenodd" d="M10.9978 14.501C10.9978 16.711 9.20615 18.5026 6.99609 18.5026C9.20615 18.5026 10.9978 20.2942 10.9978 22.5043C10.9978 20.2942 12.7894 18.5026 14.9994 18.5026C12.7894 18.5026 10.9978 16.711 10.9978 14.501Z" stroke="#D1D0FD" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </svg></div>
<span>Суть агрегатной функции в том, что она позволяет вычислить единственное значение, обработав множество строк.</span></div>
<p>Например, есть агрегатные функции, вычисляющие:</p>
<ul class="list">
<li><code style="background-color: #74992e;">count</code> (количество непустых значений);</li>
<li><code style="background-color: #74992e;">sum</code> (сумму);</li>
<li><code style="background-color: #74992e;">avg</code> (среднее);</li>
<li><code style="background-color: #74992e;">max</code> (максимум);</li>
<li><code style="background-color: #74992e;">min</code>&nbsp;(минимум) для набора строк.</li>
</ul>
<p style="text-align: center;"></p>
<p>Попробуйте в <a href="http://sql.skillfactory.ru:3000/" target="_blank" rel="noopener">Metabase</a>!</p>
<p>С помощью агрегатных функций можно найти, например, самый большой рейтинг книги:</p>
<div style="background: #74992e; overflow: auto; width: auto; max-width: 800px; border: solid #d1d9d7; border-width: .1em; border-radius: 10px; padding: .2em .6em; margin: 20px auto 20px auto;">
<pre style="margin: 0; line-height: 125%;" class="hljs language-csharp"><span class="hljs-function"><span class="hljs-keyword">select</span> <span class="hljs-title">max</span>(<span class="hljs-params">book_average_rating</span>) <span class="hljs-keyword">as</span> max_rating 
<span class="hljs-keyword">from</span> books</span>;
</pre>
</div>
<p></p>
<p><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+DS-MASTERS+01SEPT2020+type@asset+block@sql-2-1-1-1.png" width="221" height="95"></p>
<p>Запрос выдал лишь одну строку — максимальное значение колонки <code style="background-color: #74992e;">book_average_rating</code>&nbsp;из таблицы&nbsp;<code style="background-color: #74992e;">books</code>. Агрегатные функции используются, когда нужно посчитать параметры, общие для всех строк таблицы.</p>
<p>Попробуйте в <a href="http://sql.skillfactory.ru:3000/" target="_blank" rel="noopener">Metabase</a>!</p>
<p>Теперь давайте вычислим максимальный, минимальный и средний рейтинг книг в таблице, а также сумму количества оценок всех книг:</p>
<div style="background: #74992e; overflow: auto; width: auto; max-width: 800px; border: solid #d1d9d7; border-width: .1em; border-radius: 10px; padding: .2em .6em; margin: 20px auto 20px auto;">
<pre style="margin: 0; line-height: 125%;" class="hljs language-python">select <span class="hljs-built_in">max</span>(book_average_rating) <span class="hljs-keyword">as</span> max_rating
	, <span class="hljs-built_in">min</span>(book_average_rating) <span class="hljs-keyword">as</span> min_rating
	, avg(book_average_rating) <span class="hljs-keyword">as</span> average_rating
	, <span class="hljs-built_in">sum</span>(book_ratings_count) <span class="hljs-keyword">as</span> books_ratings
<span class="hljs-keyword">from</span> books;
</pre>
</div>
<p></p>
<p><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+DS-MASTERS+01SEPT2020+type@asset+block@sql-2-1-1-2.png" width="755" height="69"></p>
<p></p>
<p class="div-margin">При запросе с агрегатными функциями можно использовать условия на строки (<code style="background-color: #74992e;">WHERE</code>).</p>
<p class="div-margin">Предположим, нужно вычислить максимальный, минимальный и средний рейтинг книг в таблице, а также сумму количества оценок всех книг и количество самих книг, но только для книг,&nbsp;<code style="background-color: #74992e;">language_code</code> которых равен <code style="background-color: #74992e;">'eng'</code>:</p>
<p>Попробуйте в <a href="http://sql.skillfactory.ru:3000/" target="_blank" rel="noopener">Metabase</a>!</p>
<div style="background: #74992e; overflow: auto; width: auto; max-width: 800px; border: solid #d1d9d7; border-width: .1em; border-radius: 10px; padding: .2em .6em; margin: 20px auto 20px auto;">
<pre style="margin: 0; line-height: 125%;" class="hljs language-csharp"><span class="hljs-function"><span class="hljs-keyword">select</span> <span class="hljs-title">max</span>(<span class="hljs-params">book_average_rating</span>) <span class="hljs-keyword">as</span> max_rating
	, <span class="hljs-title">min</span>(<span class="hljs-params">book_average_rating</span>) <span class="hljs-keyword">as</span> min_rating
	, <span class="hljs-title">avg</span>(<span class="hljs-params">book_average_rating</span>) <span class="hljs-keyword">as</span> average_rating
	, <span class="hljs-title">sum</span>(<span class="hljs-params">book_ratings_count</span>) <span class="hljs-keyword">as</span> books_ratings
	, <span class="hljs-title">count</span>(<span class="hljs-params">book_id</span>) <span class="hljs-keyword">as</span> books_count
<span class="hljs-keyword">from</span> books
<span class="hljs-keyword">where</span> language_code</span> = <span class="hljs-string">'eng'</span>;
</pre>
</div>
<p></p>
<p><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+DS-MASTERS+01SEPT2020+type@asset+block@sql-2-1-1-3.png" width="912" height="68"></p>
<p>Как видим, средний рейтинг таких книг примерно равен 4, а всего таких книг 737.</p>
<p>Попробуйте в <a href="http://sql.skillfactory.ru:3000/" target="_blank" rel="noopener">Metabase</a>!</p>
<p>Агрегатным функциям также можно передавать не просто столбцы таблиц, но и их арифметические комбинации:</p>
<div style="background: #74992e; overflow: auto; width: auto; max-width: 800px; border: solid #d1d9d7; border-width: .1em; border-radius: 10px; padding: .2em .6em; margin: 20px auto 20px auto;">
<pre style="margin: 0; line-height: 125%;" class="hljs language-csharp"><span class="hljs-function"><span class="hljs-keyword">select</span> <span class="hljs-title">avg</span>(<span class="hljs-params">book_average_rating*book_average_rating + <span class="hljs-number">5</span></span>) <span class="hljs-keyword">as</span> strange_rating
<span class="hljs-keyword">from</span> books
<span class="hljs-keyword">where</span> language_code</span> = <span class="hljs-string">'eng'</span>;
</pre>
</div>
<p></p>
<p><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+DS-MASTERS+01SEPT2020+type@asset+block@sql-2-1-1-4.png" width="248" height="67"></p>
<div class="color-container container-flex blue-container">
<div class="container-icon"><svg xmlns="http://www.w3.org/2000/svg" width="26" height="26" viewBox="0 0 26 26" fill="none"> <path fill-rule="evenodd" clip-rule="evenodd" d="M6.99581 3.99658C6.99581 6.20664 5.2042 7.99825 2.99414 7.99825C5.2042 7.99825 6.99581 9.78986 6.99581 11.9999C6.99581 9.78986 8.78741 7.99825 10.9975 7.99825C8.78741 7.99825 6.99581 6.20664 6.99581 3.99658Z" stroke="#D1D0FD" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path fill-rule="evenodd" clip-rule="evenodd" d="M18.0021 16.0017C18.0021 13.2392 15.7626 10.9996 13 10.9996C15.7626 10.9996 18.0021 8.76013 18.0021 5.99756C18.0021 8.76013 20.2416 10.9996 23.0042 10.9996C20.2416 10.9996 18.0021 13.2392 18.0021 16.0017Z" stroke="#D1D0FD" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> <path fill-rule="evenodd" clip-rule="evenodd" d="M10.9978 14.501C10.9978 16.711 9.20615 18.5026 6.99609 18.5026C9.20615 18.5026 10.9978 20.2942 10.9978 22.5043C10.9978 20.2942 12.7894 18.5026 14.9994 18.5026C12.7894 18.5026 10.9978 16.711 10.9978 14.501Z" stroke="#D1D0FD" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path> </svg></div>
<span><strong>Важно:</strong> агрегатные функции <code style="background-color: #74992e;">min</code>, <code style="background-color: #74992e;">max</code>, <code style="background-color: #74992e;">count</code> можно использовать и для строковых типов данных, и для даты и времени.</span></div>
<p>Попробуйте в <a href="http://sql.skillfactory.ru:3000/" target="_blank" rel="noopener">Metabase</a>!</p>
<p>С агрегатами можно работать так же, как и с обычными столбцами. Например, их можно перемножать или делить. Предположим, нужно получить среднее арифметическое по столбцу&nbsp;<code style="background-color: #74992e;">book_average_rating</code>. Для этого можно просто использовать агрегатную функцию <code style="background-color: #74992e;">avg</code>, а можно поделить сумму рейтингов на их количество:</p>
<div style="background: #74992e; overflow: auto; width: auto; max-width: 800px; border: solid #d1d9d7; border-width: .1em; border-radius: 10px; padding: .2em .6em; margin: 20px auto 20px auto;">
<pre style="margin: 0; line-height: 125%;" class="hljs language-sql"><span class="hljs-keyword">select</span> <span class="hljs-built_in">avg</span>(book_average_rating) <span class="hljs-keyword">as</span> average_1,
	<span class="hljs-built_in">sum</span>(book_average_rating)<span class="hljs-operator">/</span><span class="hljs-built_in">count</span>(book_average_rating) average_2
<span class="hljs-keyword">from</span> books
</pre>
</div>
<p></p>
<p><img src="https://lms.skillfactory.ru/asset-v1:SkillFactory+DS-MASTERS+01SEPT2020+type@asset+block@sql-2-1-1-5.png" width="384" height="61"></p>
<p>Кстати, тут можно увидеть, как считается среднее по столбцу.</p>
<p>Попробуйте в <a href="http://sql.skillfactory.ru:3000/" target="_blank" rel="noopener">Metabase</a>!</p>
<p>Для подсчёта количества непустых строк можно использовать <code style="background-color: #74992e;">count(*)</code>:</p>
<div style="background: #74992e; overflow: auto; width: auto; max-width: 800px; border: solid #d1d9d7; border-width: .1em; border-radius: 10px; padding: .2em .6em; margin: 20px auto 20px auto;">
<pre style="margin: 0; line-height: 125%;" class="hljs language-sql"><span class="hljs-keyword">select</span> <span class="hljs-built_in">count</span>(<span class="hljs-operator">*</span>) not_null_strings_count
<span class="hljs-keyword">from</span> books
</pre>
</div>
</div>

