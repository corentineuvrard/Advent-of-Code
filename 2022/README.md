# 🎄 Advent of Code 2022 🎄

🎅 Solutions to [Advent of Code 2022](https://adventofcode.com/2022/) in Python 🐍:

| Day |          Puzzle          |          Solution          |   Parse    |   Part 1   |   Part 2   | Stars |
|:---:|:------------------------:|:--------------------------:|:----------:|:----------:|:----------:|:-----:|
|  1  |     Calorie Counting     | [day01.py](Day01/day01.py) | 0.002737 s | 0.000114 s | 0.000115 s |  ⭐⭐   |
|  2  |   Rock Paper Scissors    | [day02.py](Day02/day02.py) | 0.001959 s | 0.000904 s | 0.000920 s |  ⭐⭐   |
|  3  | Rucksack Reorganization  | [day03.py](Day03/day03.py) | 0.000450 s | 0.000485 s | 0.000322 s |  ⭐⭐   |
|  4  |       Camp Cleanup       | [day04.py](Day04/day04.py) | 0.002080 s | 0.000309 s | 0.000279 s |  ⭐⭐   |
|  5  |      Supply Stacks       | [day05.py](Day05/day05.py) | 0.001036 s | 0.000586 s | 0.000669 s |  ⭐⭐   |
|  6  |      Tuning Trouble      | [day06.py](Day06/day06.py) | 0.000156 s | 0.000771 s | 0.001458 s |  ⭐⭐   |
|  7  | No Space Left On Device  | [day07.py](Day07/day07.py) | 0.000912 s | 0.000873 s | 0.000161 s |  ⭐⭐   |
|  8  |    Treetop Tree House    | [day08.py](Day08/day08.py) | 0.001519 s | 0.003274 s | 0.023924 s |  ⭐⭐   |
|  9  |       Rope Bridge        |                            |            |            |            |
| 10  |     Cathode-Ray Tube     |                            |            |            |            |
| 11  |   Monkey in the Middle   |                            |            |            |            |
| 12  | Hill Climbing Algorithm  |                            |            |            |            |
| 13  |     Distress Signal      |                            |            |            |            |
| 14  |    Regolith Reservoir    |                            |            |            |            |
| 15  |  Beacon Exclusion Zone   |                            |            |            |            |
| 16  |  Proboscidea Volcanium   |                            |            |            |            |
| 17  |     Pyroclastic Flow     |                            |            |            |            |
| 18  |     Boiling Boulders     |                            |            |            |            |
| 19  |   Not Enough Minerals    |                            |            |            |            |
| 20  | Grove Positioning System |                            |            |            |            |
| 21  |       Monkey Math        |                            |            |            |            |
| 22  |        Monkey Map        |                            |            |            |            |
| 23  |    Unstable Diffusion    |                            |            |            |            |
| 24  |      Blizzard Basin      |                            |            |            |            |
| 25  |     Full of Hot Air      |                            |            |            |            |
|     |                          |                            |            |            |            |  16⭐  |


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
            .calendar-color-a { color: #aaaaaa; }
            .calendar-color-c { color: #eeeeee; }
            .calendar-color-d { color: #685c46; }
            .calendar-color-g0 { color: #488813; }
            .calendar-color-g1 { color: #4d8b03; }
            .calendar-color-g2 { color: #7fbd39; }
            .calendar-color-g3 { color: #427322; }
            .calendar-color-g4 { color: #01461f; }
            .calendar-color-s { color: #d0b376; }
            .calendar-color-u { color: #5eabb4; }
        </style>
    </head>
    <pre><!--
        --><span>  - /\ -  -        -       -     -      -    -          </span><br><!--          
        --><span> - /  \/\  -    -     -  -    -   -  /\   -     -       </span><br><!--
        --><span>@@@@@@@@@@#@@@@###@@@@@@@##@@@@@##@@@##@@#@@@@@@@  </span><!--
        --><span><!--
            --><span class="calendar-day">25</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@@@@@@#@@@@@@@@@@@#@@@#@@@@##@#@@@@@#@@@@@@@###@#  <!--
            --><span class="calendar-day">24</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@@@@#@@@@@##@@###@@@###@@@@@@@@@@@@@#@@@@@@##@###  <!--
            --><span class="calendar-day">23</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>#@@@@#@@@#@@@@@@@@@@@###@@@@@@@@@@#@@@@#@#@@###@@  <!--
            --><span class="calendar-day">22</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@#@##@@@@@@@@#@@@@#@@#@@#@@##@@@@@@@@#@##@@@@@@#@  <!--
            --><span class="calendar-day">21</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@@@#@@###@#@#@@@##@@@@##@#@#@@@#@@@@#@######@@#@@  <!--
            --><span class="calendar-day">20</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@@@@##@@#@@@#@@@@#@@@#@@@###@@@@@##@#@@@@@@@@@@@@  <!--
            --><span class="calendar-day">19</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@@#@@@@@###@@#@#@##@@#@#@@@@@#@@#@@#@@@@@@@#@#@#@  <!--
            --><span class="calendar-day">18</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@##@@#@@@@#@#@##@#@@@@@@@##@@@#@@@@@@##@@@##@@##@  <!--
            --><span class="calendar-day">17</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@#@@@@#@@@#@###@@@@@#@##@@@#@@@@@@@@@@@#@##@##@@#  <!--
            --><span class="calendar-day">16</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>#@##@@##@@@@@#@@@###|@@##@@@#@@@@@@@@@@@##@@@@@@@  <!--
            --><span class="calendar-day">15</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@##@#@@#@@@@@@#@@@@@@#@#@@#@##@##@@@@@@@@#@@#@###  <!--
            --><span class="calendar-day">14</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@@#@@@#@@@#@@@@@@@#@@###@@##@@@@@@@#@@@@@@@@@@@#@  <!--
            --><span class="calendar-day">13</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@@@@#@@@#@#@@#@@@@#@@#@#@##@#@@##@#@@#@#@@@@##@@#  <!--
            --><span class="calendar-day">12</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@@@###@@@#@@#@@#@#@@#@@@@#@@@@@@@@@@@@#@@@@@#@#@@  <!--
            --><span class="calendar-day">11</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@@@##@@@#@@###@@#@#@@@@@#@@@@@#@@@@@##@@@@#@@#@#@  <!--
            --><span class="calendar-day">10</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@@@#@@@#@@@<!--
            --><span class="calendar-color-s">%%%%%|</span><!--
            --><span class="calendar-color-a">_</span> <!--
            --><span class="calendar-color-g2">@</span><!--
            --><span class="calendar-color-g0">@</span><!--
            --><span class="calendar-color-g2">@@@#</span>@@#@@@@@@#@#@@@@@##@@@@@  <!--
            --><span class="calendar-day"> 9</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@@#<!--
            --><span class="calendar-color-d">|</span><!--
            --><span class="calendar-color-g3">@</span><!--
            --><span class="calendar-color-s">..</span><!--
            --><span class="calendar-color-a">/  \</span><!--
            --><span class="calendar-color-u">.~~.</span><!--
            --><span class="calendar-color-a">/  \</span><!--
            --><span class="calendar-color-s">.....</span><!--
            --><span class="calendar-color-g4">#</span><!--
            --><span class="calendar-color-g3">@</span>@@@@@##@@##@@@###@@@@@@  <!--
            --><span class="calendar-day"> 8</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>#@@<!--
            --><span class="calendar-color-g3">@</span><!--
            --><span class="calendar-color-g2">@</span><!--
            --><span class="calendar-color-g4">@</span><!--
            --><span class="calendar-color-g3">@</span><!--
            --><span class="calendar-color-g4">#</span><!--
            --><span class="calendar-color-g3">@</span><!--
            --><span class="calendar-color-g0">#</span><!--
            --><span class="calendar-color-g1">#</span><!--
            --><span class="calendar-color-u">.~~.</span><!--
            --><span class="calendar-color-g1">@</span><!--
            --><span class="calendar-color-g3">@</span><!--
            --><span class="calendar-color-g2">#</span><!--
            --><span class="calendar-color-g0">##</span><!--
            --><span class="calendar-color-g4">@</span><!--
            --><span class="calendar-color-g2">@</span><!--
            --><span class="calendar-color-g3">#</span><!--
            --><span class="calendar-color-g2">@</span><!--
            --><span class="calendar-color-s">.</span><!--
            --><span class="calendar-color-g3">@</span><!--
            --><span class="calendar-color-g4">@</span>#@@@#@@#@@@@@@@@@@##@@  <!--
            --><span class="calendar-day"> 7</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>#@#<!--
            --><span class="calendar-color-g1">@@</span><!--
            --><span class="calendar-color-g3">@#</span><!--
            --><span class="calendar-color-g1">@#</span><!--
            --><span class="calendar-color-g3">#@@</span><!--
            --><span class="calendar-color-u">.~~.</span><!--
            --><span class="calendar-color-g1">@</span><!--
            --><span class="calendar-color-g0">@</span><!--
            --><span class="calendar-color-g1">@</span><!--
            --><span class="calendar-color-g2">@</span><!--
            --><span class="calendar-color-g1">@@@</span><!--
            --><span class="calendar-color-s">..</span><!--
            --><span class="calendar-color-g4">@#</span><!--
            --><span class="calendar-color-g3">@</span><!--
            --><span class="calendar-color-g2">#</span>@@@#@#@@@@@@#@@@@@@#  <!--
            --><span class="calendar-day"> 6</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@#<!--
            --><span class="calendar-color-g3">@</span><!--
            --><span class="calendar-color-g0">@@</span><!--
            --><span class="calendar-color-g3">@</span><!--
            --><span class="calendar-color-g0">@</span><!--
            --><span class="calendar-color-g3">#</span><!--
            --><span class="calendar-color-g2">@@</span><!--
            --><span class="calendar-color-g4">@</span><!--
            --><span class="calendar-color-g3">@</span><!--
            --><span class="calendar-color-g2">@</span><!--
            --><span class="calendar-color-u">.~~.</span><!--
            --><span class="calendar-color-g3">#</span><!--
            --><span class="calendar-color-g1">#</span><!--
            --><span class="calendar-color-s">.</span><!--
            --><span class="calendar-color-c">/\</span><!--
            --><span class="calendar-color-s">.'</span><!--
            --><span class="calendar-color-g2">@</span><!--
            --><span class="calendar-color-g1">@</span><!--
            --><span class="calendar-color-g0">@</span><!--
            --><span class="calendar-color-g2">#@</span><!--
            --><span class="calendar-color-g3">@</span>@@####@@@##@@##@##@  <!--
            --><span class="calendar-day"> 5</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>@<!--
            --><span class="calendar-color-g0">@</span><!--
            --><span class="calendar-color-g1">@</span><!--
            --><span class="calendar-color-g0">##</span><!--
            --><span class="calendar-color-g1">@</span><!--
            --><span class="calendar-color-g0">#</span><!--
            --><span class="calendar-color-g3">@</span><!--
            --><span class="calendar-color-g1">@</span><!--
            --><span class="calendar-color-g2">@</span><!--
            --><span class="calendar-color-g0">@</span><!--
            --><span class="calendar-color-s">.'</span><!--
            --><span class="calendar-color-u"> ~  </span><!--
            --><span class="calendar-color-s">'.</span><!--
            --><span class="calendar-color-c">/\</span><!--
            --><span class="calendar-color-s">'.</span><!--
            --><span class="calendar-color-c">/\</span><!--
            --><span class="calendar-color-s">' .</span><!--
            --><span class="calendar-color-g1">@</span><!--
            --><span class="calendar-color-g2">@@</span>|@#@###@#@@@@#@#@@  <!--
            --><span class="calendar-day"> 4</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-g2">@@</span><!--
            --><span class="calendar-color-g4">#</span><!--
            --><span class="calendar-color-g2">@</span><!--
            --><span class="calendar-color-g4">#</span><!--
            --><span class="calendar-color-g0">@</span><!--
            --><span class="calendar-color-g1">@</span><!--
            --><span class="calendar-color-g2">@</span><!--
            --><span class="calendar-color-g0">@</span><!--
            --><span class="calendar-color-s">_/</span><!--
            --><span class="calendar-color-u"> ~   ~  </span><!--
            --><span class="calendar-color-s">\ ' '. '.'.</span><!--
            --><span class="calendar-color-g0">@@</span>@##@#@@@@@@#@@#@@  <!--
            --><span class="calendar-day"> 3</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-s">-~------'</span><!--
            --><span class="calendar-color-u">    ~    ~ </span><!--
            --><span class="calendar-color-s">'--~-----~-~----___________--</span>  <!--
            --><span class="calendar-day"> 2</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-u">  ~    ~  ~      ~     ~ ~   ~     ~  ~  ~   ~   </span>  <!--
            --><span class="calendar-day"> 1</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><!--
    --></pre>
</html>
