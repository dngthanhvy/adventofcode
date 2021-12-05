using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AdventOfCode {
    public static class Day1 {

        public static List<int> ReadInput( string inputPath ) {

            List<int> list = new List<int>();
            try {
                foreach ( string line in File.ReadLines(inputPath) ) {
                    list.Add(Int16.Parse(line));
                }
                return list;
            } catch (Exception) {
                throw new Exception("The file doesn't exist.");
            }
        }

        public static int GetNumberOfIncreasedDepth( List<int> inputList ) {
            int count = 0; // the number of measurements that are larger than the previous measurement
            for ( int i = 1; i<inputList.Count; i++ ) {
                if ( inputList[i]>inputList[i-1] ) count++;
            }
            return count;
        }

        public static int CompareSlidingMeasurementWindow(List<int> inputList) {
            int lastSum = inputList[0]+inputList[1]+inputList[2];
            int currentSum = 0;
            int count = 0;
            for (int i = 1; i < inputList.Count; i++) {
                if (inputList.Count - 1 - i < 2 ) return count;
                for (int j = 0; j < 3; j++ ) {
                    currentSum+=inputList[i+j];
                }
                if ( currentSum>lastSum ) count++;
                //Console.WriteLine($"Current: {currentSum}\tLast: {lastSum}\tCount: {count}");
                lastSum=currentSum;
                currentSum=0;
            }
            return count;
        } 
    }
}
