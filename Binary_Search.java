package com.ProDuctive;

public class Binary_Search {
    public static void main(String[] args) {
         int[] our_array = new int[100];
         for (int i = 0; i<100; i++){
             our_array[i] = i;
         }
        System.out.println(Bin(our_array, 120));


    }
    public static int Bin(int[] arr, int val){
        int l = 0;
        int u = arr.length-1;
        int i = (l+u)/2;

        while(l<=u){

            if (arr[i] == val){
                return i;
            }
            else if (arr[i] < val){
                l = i+1;
                i = (l+u)/2;
                continue;
            }
            else if (arr[i] > val){
                u = i-1;
                i = (l+u)/2;
                continue;
            }
        }
        return -1;



    }

}
