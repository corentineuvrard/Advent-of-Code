# 🎄 Advent of Code 2021 🎄

🎅 Solutions to [Advent of Code 2021](https://adventofcode.com/2021/) in Python 🐍:

| Day |         Puzzle          |          Solution          |   Parse    |   Part 1   |   Part 2   | Stars |
|:---:|:-----------------------:|:--------------------------:|:----------:|:----------:|:----------:|:-----:|
|  1  |       Sonar Sweep       | [day01.py](Day01/day01.py) | 0.001113 s | 0.000345 s | 0.000318 s |  ⭐⭐   |
|  2  |          Dive!          | [day02.py](Day02/day02.py) | 0.004287 s | 0.000174 s | 0.000214 s |  ⭐⭐   |
|  3  |    Binary Diagnostic    | [day03.py](Day03/day03.py) | 0.000570 s | 0.000876 s | 0.005034 s |  ⭐⭐   |
|  4  |       Giant Squid       | [day04.py](Day04/day04.py) | 0.003202 s | 0.007498 s | 0.009233 s |  ⭐⭐   |
|  5  |  Hydrothermal Venture   | [day05.py](Day05/day05.py) | 0.004635 s | 0.615970 s | 0.998271 s |  ⭐⭐   |
|  6  |       Lanternfish       | [day06.py](Day06/day06.py) | 0.000499 s | 0.000087 s | 0.000188 s |  ⭐⭐   |
|  7  | The Treachery of Whales | [day07.py](Day07/day07.py) | 0.000795 s | 0.000378 s | 0.020677 s |  ⭐⭐   |
|  8  |  Seven Segment Search   | [day08.py](Day08/day08.py) | 0.001026 s | 0.000171 s | 0.010321 s |  ⭐⭐   |
|  9  |       Smoke Basin       | [day09.py](Day09/day09.py) | 0.003076 s | 0.027139 s | 0.123556 s |  ⭐⭐   |
| 10  |     Syntax Scoring      | [day10.py](Day10/day10.py) | 0.000278 s | 0.002305 s | 0.002455 s |  ⭐⭐   |
| 11  |      Dumbo Octopus      | [day11.py](Day11/day11.py) | 0.000230 s | 0.019426 s | 0.051653 s |  ⭐⭐   |
| 12  |     Passage Pathing     | [day12.py](Day12/day12.py) | 0.000223 s | 0.018712 s | 0.333444 s |  ⭐⭐   |
| 13  |   Transparent Origami   | [day13.py](Day13/day13.py) | 0.182104 s | 0.023175 s | 0.031994 s |  ⭐⭐   |
| 14  | Extended Polymerization | [day14.py](Day14/day14.py) | 0.004348 s | 0.029037 s | 0.096075 s |  ⭐⭐   |
| 15  |         Chiton          | [day15.py](Day15/day15.py) | 0.004116 s | 0.133478 s | 2.881320 s |  ⭐⭐   |
| 16  |     Packet Decoder      | [day16.py](Day16/day16.py) | 0.026500 s | 0.028636 s | 0.025613 s |  ⭐⭐   |
| 17  |       Trick Shot        | [day17.py](Day17/day17.py) | 0.000685 s | 0.000053 s | 0.769676 s |  ⭐⭐   |
| 18  |        Snailfish        |                            |            |            |            |       |
| 19  |     Beacon Scanner      |                            |            |            |            |       |
| 20  |       Trench Map        |                            |            |            |            |       |
| 21  |       Dirac Dice        |                            |            |            |            |       |
| 22  |     Reactor Reboot      |                            |            |            |            |       |
| 23  |        Amphipod         |                            |            |            |            |       |
| 24  |  Arithmetic Logic Unit  |                            |            |            |            |       |
| 25  |      Sea Cucumber       |                            |            |            |            |       |
|     |                         |                            |            |            |            |  34⭐  |


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
            .calendar-color-g { color: #a47a4d; }
            .calendar-color-o { color: #c74c30; }
            .calendar-color-r { color: #ff0000; }
            .calendar-color-s { color: #ffffff; }
            .calendar-color-w1 { color: #00c8ff; }
            .calendar-color-w2 { color: #00b5ed; }
            .calendar-color-w3 { color: #00a2db; }
            .calendar-color-w4 { color: #0091cc; }
            .calendar-color-w5 { color: #0085c0; }
            .calendar-color-w6 { color: #0079b5; }
            .calendar-color-w7 { color: #006daa; }
            .calendar-color-w8 { color: #00619f; }
            .calendar-color-w9 { color: #005a98; }
            .calendar-color-w10 { color: #005291; }
            .calendar-color-w11 { color: #004a8a; }
            .calendar-color-w12 { color: #004282; }
            .calendar-color-w13 { color: #003b7b; }
            .calendar-color-w14 { color: #003374; }
            .calendar-color-w15 { color: #002e6f; }
            .calendar-color-w16 { color: #00296b; }
            .calendar-color-w17 { color: #002566; }
        </style>
    </head>
    <pre><!--
        --><span><!--
            --><span class="calendar-color-w1">~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~</span>  <!--
            --><span class="calendar-day"> 1</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w2">    .  '     ..  .   ..       ..</span> <!--
            --><span class="calendar-color-s">.</span> <!--
            --><span class="calendar-color-w2">.      </span> <!--
            --><span class="calendar-color-g">..''''</span>  <!--
            --><span class="calendar-day"> 2</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w3">     .. .  ..'     '        ...</span> <!--
            --><span class="calendar-color-s">.</span> <!--
            --><span class="calendar-color-w3"> ~.    </span> <!--
            --><span class="calendar-color-g">:</span>        <!--
            --><span class="calendar-day"> 3</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w4"> ..         .  '  .      .  .  </span> <!--
            --><span class="calendar-color-s">.'</span> <!--
            --><span class="calendar-color-w4">  </span> <!--
            --><span class="calendar-color-g">....'</span>        <!--
            --><span class="calendar-day"> 4</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w5">.  . ..   '  .  '    .''     </span> <!--
            --><span class="calendar-color-o">.</span><!--
            --><span class="calendar-color-r">.</span><!--
            --><span class="calendar-color-s">|\</span><!--
            --><span class="calendar-color-r">.</span><!--
            --><span class="calendar-color-o">.</span><!--
            --><span class="calendar-color-g">''</span>             <!--
            --><span class="calendar-day"> 5</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w6">   .              '.  . .   </span> <!--
            --><span class="calendar-color-g">:</span>                     <!--
            --><span class="calendar-day"> 6</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
            --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w7">     ~  .    .   .       .</span> <!--
            --><span class="calendar-color-g">:'</span>                      <!--
            --><span class="calendar-day"> 7</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
            --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w8"> .      .         .     . </span>  <!--
            --><span class="calendar-color-g">'''''.....</span>  <!--
            --><span class="calendar-color-g">..</span><!--
            --><span class="calendar-color-o">.</span><!--
            --><span class="calendar-color-r">.</span>       <!--
            --><span class="calendar-day"> 8</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w9">            .   .    ~ ..</span> <!--
            --><span class="calendar-color-g">:'..</span>  <!--
            --><span class="calendar-color-g">..</span>    <!--
            --><span class="calendar-color-g">''</span>    <!--
            --><span class="calendar-color-r">':</span>     <!--
            --><span class="calendar-day"> 9</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w10">  .      .    .   .  .   </span> <!--
            --><span class="calendar-color-g">:</span>   <!--
            --><span class="calendar-color-g">''</span>  <!--
            --><span class="calendar-color-g">''''..</span>     <!--
            --><span class="calendar-color-o">'</span><!--
            --><span class="calendar-color-g">.</span>    <!--
            --><span class="calendar-day">10</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w11">   .  .          .   .   </span> <!--
            --><span class="calendar-color-g">:</span>             <!--
            --><span class="calendar-color-g">'..'.</span> <!--
            --><span class="calendar-color-g">:</span>    <!--
            --><span class="calendar-day">11</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w12">. . '  '    .~       . .</span> <!--
            --><span class="calendar-color-g">:</span>       <!--
            --><span class="calendar-color-g">:'''..</span>   <!--
            --><span class="calendar-color-g">..'</span> <!--
            --><span class="calendar-color-g">:</span>    <!--
            --><span class="calendar-day">12</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w13">   .    ..            </span> <!--
            --><span class="calendar-color-g">.'</span>    <!--
            --><span class="calendar-color-g">..''</span>      <!--
            --><span class="calendar-color-g">'''</span> <!--
            --><span class="calendar-color-g">...:</span>    <!--
            --><span class="calendar-day">13</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w14"> . .  .   '   .      </span> <!--
            --><span class="calendar-color-g">:</span> <!--
            --><span class="calendar-color-g">...''</span>  <!--
            --><span class="calendar-color-g">..':</span>   <!--
            --><span class="calendar-color-r">.</span><!--
            --><span class="calendar-color-o">.</span><!--
            --><span class="calendar-color-g">..'</span>        <!--
            --><span class="calendar-day">14</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-w15"> .         .   .  ~  </span> <!--
            --><span class="calendar-color-g">:'</span> <!--
            --><span class="calendar-color-g">...'''</span>    <!--
            --><span class="calendar-color-o">'</span><!--
            --><span class="calendar-color-r">''</span>             <!--
            --><span class="calendar-day">15</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span><!--
            --><span class="calendar-color-g">'.'.</span> <!--
            --><span class="calendar-color-w16">   '    . </span> <!--
            --><span class="calendar-color-g">:'.</span> <!--
            --><span class="calendar-color-g">....'</span>                          <!--
            --><span class="calendar-day">16</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>   <!--
            --><span class="calendar-color-g">:</span> <!--
            --><span class="calendar-color-w17">.         </span> <!--
            --><span class="calendar-color-g">:</span>  <!--
            --><span class="calendar-color-g">'</span>                               <!--
            --><span class="calendar-day">17</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>   :        . ..'                                  <!--
            --><span class="calendar-day">18</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>   '. . . .   :                                    <!--
            --><span class="calendar-day">19</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>    '.        :                                    <!--
            --><span class="calendar-day">20</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>      :  .   :                                     <!--
            --><span class="calendar-day">21</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>      '.  .  :                                     <!--
            --><span class="calendar-day">22</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>       : .  .'                                     <!--
            --><span class="calendar-day">23</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>       :   .'                                      <!--
            --><span class="calendar-day">24</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><br><!--
        --><span>       :..:                                        <!--
            --><span class="calendar-day">25</span> <!--
            --><span>*</span><!--
            --><span>*</span><!--
        --></span><!--
    --></pre>
</html>
