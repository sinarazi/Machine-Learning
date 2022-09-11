package com.company;

import java.io.IOException;
import java.util.ArrayList;


public class Main {
        public static  ArrayList<Integer> AND_hebb () {
            int w_1 = 0, w_2 = 0, b = 0; // Initialize first values
            int[][] and_Entry = {{1, 1, 1},
                                {1, -1, -1},
                                {-1, 1, -1},
                                {-1, -1, -1}};

            ArrayList<Integer> arr = new ArrayList<>();
            ArrayList<Integer> arr1 = new ArrayList<>();
            int counter1 = 1;
            for (int[] i : and_Entry) {
                w_1 += i[0] * i[2];
                w_2 += i[1] * i[2];
                b += i[2]; // setting Bias
                // step by step hebbian algorithm
                arr1.add(w_1);
                arr1.add(w_2);
                arr1.add(b);
                System.out.println("The step " + (counter1++)+" is: "+ arr1);
                arr1.clear();
                int counter = 0;

                for (int[] j : and_Entry) {

                    if ((j[0] * w_1 + j[1] * w_2 + b <= 0 && j[2] == -1) // both of them inactive
                            || (j[0] * w_1 + j[1] * w_2 + b > 0 && j[2] == 1)) { // both of them active
                        counter += 1; // to iterate foreach

                    }
                    int size = arr.size();
                    if (counter == 4 && size == 0) {
                        arr.add(w_1);
                        arr.add(w_2);
                        arr.add(b);
                        System.out.println("Final result: " + arr);
                    }
                }
                Plot plot = Plot.plot(null).
                        // setting data
                                series(null, Plot.data().

                                xy(1, -1).

                                xy(-1, 2),null);

                try {
                    plot.save("and", "png");
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return arr;
        }

        public static ArrayList<Integer> OR_hebb() {
            int w_1 = 0, w_2 = 0, b = 0; // Initialize first values
            int[][] and_Entry = {{1, 1, 1},
                    {1, -1, 1},
                    {-1, 1, 1},
                    {-1, -1, -1}};
            //int[] arr;
            ArrayList<Integer> arr = new ArrayList<>();
            ArrayList<Integer> arr1 = new ArrayList<>();
            int counter1 = 1;
            for (int[] i : and_Entry) {
                w_1 += i[0] * i[2];
                w_2 += i[1] * i[2];
                b += i[2]; // setting Bias
                // step by step hebbian algorithm
                arr1.add(w_1);
                arr1.add(w_2);
                arr1.add(b);
                System.out.println("The step " + (counter1++)+" is: "+ arr1);
                arr1.clear();
                int counter = 0;
                for (int[] j : and_Entry) {
                    if ((j[0] * w_1 + j[1] * w_2 + b <= 0 && j[2] == -1) // both of them inactive
                            || (j[0] * w_1 + j[1] * w_2 + b > 0 && j[2] == 1)) { // both of them active
                        counter += 1; // to iterate foreach
                    }
                    int size = arr.size();
                    if (counter == 4 && size == 0) {
                        arr.add(w_1);
                        arr.add(w_2);
                        arr.add(b);
                        System.out.println(arr);
                    }
                }
                Plot plot = Plot.plot(null).
                        // setting data
                                series(null, Plot.data().

                                xy(1, -2).

                                xy(-2, 1),null);

                try {
                    plot.save("or", "png");
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return arr;
        }

    public static void main(String[] args) {
	// write your code here
        ArrayList<Integer> and = AND_hebb();
        System.out.println("AND : (" + and.get(0) + ")" + "X1 + " +
                            "(" + and.get(1) + ")" + "X2 + " +
                            "(" + and.get(2) + ")" + "b = 0");
        ArrayList<Integer> or = OR_hebb();
        System.out.println("OR : (" + or.get(0) + ")" + "X1 + " +
                            "(" + or.get(1) + ")" + "X2 + " +
                            "(" + or.get(2) + ")" + "b = 0");

    }
}



