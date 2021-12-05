using System;
using System.Collections.Generic;

namespace AdventOfCode {
    class Program {

        static void Day1Test2021() {
            List<int> input = Day1.ReadInput(@"..\..\..\Day1\inputs\day1.txt");
            int numberOfIncreasingDepth = Day1.GetNumberOfIncreasedDepth(input);
            int numberOfIncreasingSlidingWindows = Day1.CompareSlidingMeasurementWindow(input);
            Console.WriteLine(numberOfIncreasingSlidingWindows);
        }

        static void Day2Test2021() {
            List<string> input = Day2.ReadInput(@"..\..\..\Day2\inputs\day2.txt");
            Day2.FollowTheMap(input);
        }

        static void Main( string[] args ) {
            Day2Test2021();
        }
    }
}
