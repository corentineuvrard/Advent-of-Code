# 🎄 Advent of Code 2024 🎄

🎅 Solutions to [Advent of Code 2024](https://adventofcode.com/2024/) in Python 🐍:

| Day |        Puzzle         |          Solution          |   Parse    |   Part 1   |   Part 2   | Stars |
|:---:|:---------------------:|:--------------------------:|:----------:|:----------:|:----------:|:-----:|
|  1  |  Historian Hysteria   | [day01.py](Day01/day01.py) | 0.000960 s | 0.000709 s | 0.000804 s |  ⭐⭐   |
|  2  |   Red-Nosed Reports   | [day02.py](Day02/day02.py) | 0.001847 s | 0.000889 s | 0.002511 s |  ⭐⭐   |
|  3  |     Mull It Over      | [day03.py](Day03/day03.py) | 0.000215 s | 0.000711 s | 0.000841 s |  ⭐⭐   |
|  4  |     Ceres Search      | [day04.py](Day04/day04.py) | 0.000246 s | 0.029387 s | 0.003271 s |  ⭐⭐   |
|  5  |      Print Queue      | [day05.py](Day05/day05.py) | 0.001730 s | 0.002207 s | 0.007895 s |  ⭐⭐   |
|  6  |  Guardian Gallivant   | [day06.py](Day06/day06.py) | 0.000505 s | 0.004033 s | 1.523398 s |  ⭐⭐   |
|  7  |     Bridge Repair     | [day07.py](Day07/day07.py) | 0.001860 s | 0.099068 s | 5.751030 s |  ⭐⭐   |
|  8  | Resonant Collinearity |                            |            |            |            |       |
|  9  |    Disk Fragmenter    |                            |            |            |            |       |
| 10  |        Hoof It        |                            |            |            |            |       |
| 11  |                       |                            |            |            |            |       |
| 12  |                       |                            |            |            |            |       |
| 13  |                       |                            |            |            |            |       |
| 14  |                       |                            |            |            |            |       |
| 15  |                       |                            |            |            |            |       |
| 16  |                       |                            |            |            |            |       |
| 17  |                       |                            |            |            |            |       |
| 18  |                       |                            |            |            |            |       |
| 19  |                       |                            |            |            |            |       |
| 20  |                       |                            |            |            |            |       |
| 21  |                       |                            |            |            |            |       |
| 22  |                       |                            |            |            |            |       |
| 23  |                       |                            |            |            |            |       |
| 24  |                       |                            |            |            |            |       |
| 25  |                       |                            |            |            |            |       |
|     |                       |                            |            |            |            |  14⭐  |


<html>
    <head>
        <style>
            body { 
                display: inline-block;
                text-align: center;
            }
            a { color: #f0f6fc; }
            pre {
                display: inline-block;
                color: #666666;
                background-color: #0f0f23;
            }
            .calendar-day { color: #cccccc; }
            .calendar-mark-complete { color: #ffff66; }
            .calendar-mark-verycomplete { color: #ffff66; }
            .calendar-color-2g0 { color: #488813; }
            .calendar-color-2g1 { color: #4d8b03; }
            .calendar-color-2g2 { color: #7fbd39; }
            .calendar-color-2g3 { color: #427322; }
            .calendar-color-2g4 { color: #01461f; }
            .calendar-color-2u { color: #5eabb4; }
            .calendar-color-2w { color: #ffffff; }
            .calendar-color-3a { color: #a5a8af; }
            .calendar-color-3b { color: #5555bb; }
            .calendar-color-3g { color: #00cc00; }
            .calendar-color-3i { color: #a25151; }
            .calendar-color-3l { color: #ccccff; }
            .calendar-color-3m { color: #d4dde4; }
            .calendar-color-3s { color: #e3b585; }
            .calendar-color-3w { color: #ffffff; }
            .calendar-color-3y {
                color: #ffff66;
                text-shadow: 0 0 5px #ffff66, 0 0 10px #ffff66;
            }
            .calendar-color-6b { color: #009900; }
            .calendar-color-6o {
                color: #ff9900;
                text-shadow: 0 0 5px #ff9900;
            }
            .calendar-color-6r {
                color: #ff0000;
                text-shadow: 0 0 5px #ff0000;
            }
            .calendar-color-6t { color: #aaaaaa; }
            .calendar-color-6u {
                color: #0066ff;
                text-shadow: 0 0 5px #0066ff;
            }
            .calendar-color-6y {
                color: #ffff66;
                text-shadow: 0 0 5px #ffff66;
            }
            .calendar-color-8e { color: #cccccc; }
            .calendar-color-8i {
                color: #ff0000;
                text-shadow: 0 0  5px #ff0000, 0 0 10px #ff0000, 0 0 15px #ff0000;
            }
            .calendar-color-8n { color: #886655; }
            .calendar-color-8w { color: #cccccc; }
            .calendar-color-w { color: #cccccc; }
        </style>
    </head>
    <pre><!--
        --><span> .-----.          .------------------.</span><br><!--
        --><span>       <!--
            --><span class="calendar-color-w">.--'</span><!--
            --><span class="calendar-color-3s">~</span> <!--
            --><span class="calendar-color-3s">~</span> <!--
            --><span class="calendar-color-3s">~</span><!--
            --><span class="calendar-color-w">|</span>        <!--
            --><span class="calendar-color-w">.-'</span> <!--
            --><span class="calendar-color-6y">*</span>       <!--
            --><span class="calendar-color-8n">\</span>  <!--
            --><span class="calendar-color-8n">/</span>     <!--
            --><span class="calendar-color-w">'-.</span>  <!--
            --><span class="calendar-day"> 1</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>    <!--
            --><span class="calendar-color-w">.--'</span><!--
            --><span class="calendar-color-3s">~</span>  <!--
            --><span class="calendar-color-3g">,</span><!--
            --><span class="calendar-color-3y">*</span> <!--
            --><span class="calendar-color-3s">~</span> <!--
            --><span class="calendar-color-w">|</span>        <!--
            --><span class="calendar-color-w">|</span>  <!--
            --><span class="calendar-color-6b">&gt;</span><!--
            --><span class="calendar-color-6o">o</span><!--
            --><span class="calendar-color-6b">&lt;</span>   <!--
            --><span class="calendar-color-8n">\_\_\|_/__/</span>   <!--
            --><span class="calendar-color-w">|</span>  <!--
            --><span class="calendar-day"> 2</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w">.---'</span><!--
            --><span class="calendar-color-3s">:</span> <!--
            --><span class="calendar-color-3s">~</span> <!--
            --><span class="calendar-color-3g">'</span><!--
            --><span class="calendar-color-3b">(~)</span><!--
            --><span class="calendar-color-3g">,</span> <!--
            --><span class="calendar-color-3s">~</span><!--
            --><span class="calendar-color-w">|</span>        <!--
            --><span class="calendar-color-w">|</span> <!--
            --><span class="calendar-color-6b">&gt;</span><!--
            --><span class="calendar-color-6r">@</span><!--
            --><span class="calendar-color-6b">&gt;</span><!--
            --><span class="calendar-color-6u">O</span><!--
            --><span class="calendar-color-6b">&lt;</span> <!--
            --><span class="calendar-color-8i">o</span><!--
            --><span class="calendar-color-8n">-_/</span><!--
            --><span class="calendar-color-8e">.</span><!--
            --><span class="calendar-color-8w">()</span><!--
            --><span class="calendar-color-8n">__------</span><!--
            --><span class="calendar-color-w">|</span>  <!--
            --><span class="calendar-day"> 3</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w">|</span><!--
            --><span class="calendar-color-2g2">#</span><!--
            --><span class="calendar-color-2u">..</span><!--
            --><span class="calendar-color-2g2">@</span><!--
            --><span class="calendar-color-3s">'.</span> <!--
            --><span class="calendar-color-3s">~</span> <!--
            --><span class="calendar-color-3g">"</span> <!--
            --><span class="calendar-color-3g">'</span> <!--
            --><span class="calendar-color-3s">~</span> <!--
            --><span class="calendar-color-w">|</span>        <!--
            --><span class="calendar-color-w">|</span><!--
            --><span class="calendar-color-6b">&gt;</span><!--
            --><span class="calendar-color-6u">O</span><!--
            --><span class="calendar-color-6b">&gt;</span><!--
            --><span class="calendar-color-6o">o</span><!--
            --><span class="calendar-color-6b">&lt;</span><!--
            --><span class="calendar-color-6r">@</span><!--
            --><span class="calendar-color-6b">&lt;</span> <!--
            --><span class="calendar-color-8n">\____</span>       <!--
            --><span class="calendar-color-3g">.'</span><!--
            --><span class="calendar-color-w">|</span>  <!--
            --><span class="calendar-day"> 4</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w">|</span><!--
            --><span class="calendar-color-2g2">_</span><!--
            --><span class="calendar-color-2u">.~.</span><!--
            --><span class="calendar-color-2g2">_</span><!--
            --><span class="calendar-color-2g3">@</span><!--
            --><span class="calendar-color-3s">'..</span> <!--
            --><span class="calendar-color-3s">~</span> <!--
            --><span class="calendar-color-3s">~</span> <!--
            --><span class="calendar-color-3y">*</span><!--
            --><span class="calendar-color-w">|</span>        <!--
            --><span class="calendar-color-w">|</span> <!--
            --><span class="calendar-color-6t">_|</span> <!--
            --><span class="calendar-color-6t">|_</span>    <!--
            --><span class="calendar-color-w">..</span><!--
            --><span class="calendar-color-8w">\_</span><!--
            --><span class="calendar-color-8n">\_</span> <!--
            --><span class="calendar-color-3g">..'</span><!--
            --><span class="calendar-color-3y">*</span> <!--
            --><span class="calendar-color-w">|</span>  <!--
            --><span class="calendar-day"> 5</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w">|</span> <!--
            --><span class="calendar-color-2w">|||</span> <!--
            --><span class="calendar-color-2g2">#</span><!--
            --><span class="calendar-color-2g4">@</span><!--
            --><span class="calendar-color-2g1">@</span><!--
            --><span class="calendar-color-2g0">@</span><!--
            --><span class="calendar-color-3s">'''...</span><!--
            --><span class="calendar-color-w">|</span>        <!--
            --><span class="calendar-color-w">|</span><!--
            --><span class="calendar-color-3i">...</span>     <!--
            --><span class="calendar-color-w">.'</span>  <!--
            --><span class="calendar-color-w">'.</span><!--
            --><span class="calendar-color-3g">'''..</span><!--
            --><span class="calendar-color-3m">/</span><!--
            --><span class="calendar-color-3g">..</span><!--
            --><span class="calendar-color-w">|</span>  <!--
            --><span class="calendar-day"> 6</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w">|</span><!--
            --><span class="calendar-color-2g1">@</span><!--
            --><span class="calendar-color-2w">~~~</span><!--
            --><span class="calendar-color-2g3">#</span><!--
            --><span class="calendar-color-2g0">@</span><!--
            --><span class="calendar-color-2g1">#</span><!--
            --><span class="calendar-color-2g3">@</span><!--
            --><span class="calendar-color-2g4">@@</span><!--
            --><span class="calendar-color-2g3">@</span>    <!--
            --><span class="calendar-color-w">|</span>        <!--
            --><span class="calendar-color-w">|</span><!--
            --><span class="calendar-color-3a">/\</span> <!--
            --><span class="calendar-color-3i">''.</span>  <!--
            --><span class="calendar-color-w">|</span>    <!--
            --><span class="calendar-color-w">|</span>   <!--
            --><span class="calendar-color-3l">-</span><!--
            --><span class="calendar-color-3m">/</span>  <!--
            --><span class="calendar-color-3w">:</span><!--
            --><span class="calendar-color-w">|</span>  <!--
            --><span class="calendar-day"> 7</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>|   .--.        |        |        |    |        |  <!--
            --><span class="calendar-day"> 8</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>'---'  |        |        |        |    |        |  <!--
            --><span class="calendar-day"> 9</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>       |        |        |        |    |        |  <!--
            --><span class="calendar-day">10</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>       |        |        |        |    |        |  <!--
            --><span class="calendar-day">11</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>                                                   <!--
            --><span class="calendar-day">12</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>                                                   <!--
            --><span class="calendar-day">13</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>                                                   <!--
            --><span class="calendar-day">14</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>                                                   <!--
            --><span class="calendar-day">15</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>                                                   <!--
            --><span class="calendar-day">16</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>                                                   <!--
            --><span class="calendar-day">17</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>                                                   <!--
            --><span class="calendar-day">18</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>                                                   <!--
            --><span class="calendar-day">19</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>                                                   <!--
            --><span class="calendar-day">20</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>                                                   <!--
            --><span class="calendar-day">21</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>                                                   <!--
            --><span class="calendar-day">22</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>                                                   <!--
            --><span class="calendar-day">23</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>                                                   <!--
            --><span class="calendar-day">24</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>                                                   <!--
            --><span class="calendar-day">25</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
    --></pre>
</html>
