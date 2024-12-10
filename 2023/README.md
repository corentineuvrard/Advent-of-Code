# 🎄 Advent of Code 2023 🎄

🎅 Solutions to [Advent of Code 2023](https://adventofcode.com/2023/) in Python 🐍:

| Day |             Puzzle              |          Solution          |   Parse    |   Part 1   |   Part 2   | Stars |
|:---:|:-------------------------------:|:--------------------------:|:----------:|:----------:|:----------:|:-----:|
|  1  |           Trebuchet?!           | [day01.py](Day01/day01.py) | 0.000484 s | 0.002045 s | 0.005920 s |  ⭐⭐   |
|  2  |         Cube Conundrum          | [day02.py](Day02/day02.py) | 0.001736 s | 0.000103 s | 0.000131 s |  ⭐⭐   |
|  3  |           Gear Ratios           |                            |            |            |            |       |
|  4  |          Scratchcards           |                            |            |            |            |       |
|  5  | If You Give A Seed A Fertilizer |                            |            |            |            |       |
|  6  |           Wait For It           |                            |            |            |            |       |
|  7  |           Camel Cards           |                            |            |            |            |
|  8  |        Haunted Wasteland        |                            |            |            |            |
|  9  |       Mirage Maintenance        |                            |            |            |            |
| 10  |            Pipe Maze            |                            |            |            |            |
| 11  |        Cosmic Expansion         |                            |            |            |            |
| 12  |           Hot Springs           |                            |            |            |            |
| 13  |       Point of Incidence        |                            |            |            |            |
| 14  |    Parabolic Reflector Dish     |                            |            |            |            |
| 15  |          Lens Library           |                            |            |            |            |
| 16  |     The Floor Will Be Lava      |                            |            |            |            |
| 17  |         Clumsy Crucible         |                            |            |            |            |
| 18  |         Lavaduct Lagoon         |                            |            |            |            |
| 19  |             Aplenty             |                            |            |            |            |
| 20  |        Pulse Propagation        |                            |            |            |            |
| 21  |          Step Counter           |                            |            |            |            |
| 22  |           Sand Slabs            |                            |            |            |            |
| 23  |           A Long Walk           |                            |            |            |            |
| 24  |     Never Tell Me The Odds      |                            |            |            |            |
| 25  |           Snowverload           |                            |            |            |            |
|     |                                 |                            |            |            |            |  4⭐   |


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
            .calendar-color-l { color: #ccccff; }
            .calendar-color-n { color: #9b715b; }
            .calendar-color-w { color: #ffffff; }
            .calendar-color-y { 
                color: #ffff66;
                text-shadow: 0 0 5px #ffff66, 0 0 10px #ffff66;
            }
        </style>
    <pre><!--
        --><span>                         *                         <!--
            --><span class="calendar-day">14</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>                                 *                 <!--
            --><span class="calendar-day">15</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>                                    *              <!--
            --><span class="calendar-day">16</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>                        *                          <!--
            --><span class="calendar-day">13</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>              *                                    <!--
            --><span class="calendar-day">17</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>        *                                          <!--
            --><span class="calendar-day">12</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>                 *                                 <!--
            --><span class="calendar-day">18</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>      *                                            <!--
            --><span class="calendar-day">11</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>            *                                      <!--
            --><span class="calendar-day">10</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>                      *                            <!--
            --><span class="calendar-day">19</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>               *                                   <!--
            --><span class="calendar-day"> 9</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>                    *                              <!--
            --><span class="calendar-day"> 8</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>                       *                           <!--
            --><span class="calendar-day">20</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>                  *                                <!--
            --><span class="calendar-day"> 7</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>                                  *                <!--
            --><span class="calendar-day"> 6</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>                                        *          <!--
            --><span class="calendar-day">21</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>                                           *       <!--
            --><span class="calendar-day"> 5</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>                            *                      <!--
            --><span class="calendar-day">22</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>                                   *               <!--
            --><span class="calendar-day"> 4</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>               *                                   <!--
            --><span class="calendar-day">23</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>                        *                          <!--
            --><span class="calendar-day">25</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>            <!--
            --><span class="calendar-color-w">'</span>       *     <!--
            --><span class="calendar-color-l">-</span>                        <!--
            --><span class="calendar-day">24</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>              <!--
            --><span class="calendar-color-w">'</span> <!--
            --><span class="calendar-color-w">.</span>    <!--
            --><span class="calendar-color-l">-</span>     <!--
            --><span class="calendar-color-l">-</span>   * <!--
            --><span class="calendar-color-w">.</span>                 <!--
            --><span class="calendar-day"> 3</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>    <!--
            --><span class="calendar-color-n">----@</span>        <!--
            --><span class="calendar-color-w">'''..</span><!--
            --><span class="calendar-color-y">*</span><!--
            --><span class="calendar-color-w">......'''</span>                   <!--
            --><span class="calendar-day"> 2</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><br><!--
        --><span>  <!--
            --><span class="calendar-color-y">*</span> <!--
            --><span class="calendar-color-n">!</span> <!--
            --><span class="calendar-color-n">/^\</span>                                          <!--
            --><span class="calendar-day"> 1</span> <!--
            --><span class="calendar-mark-complete">*</span><!--
            --><span class="calendar-mark-verycomplete">*</span><!--
        --></span><!--
    --></pre>
</html>
