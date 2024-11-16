// Given an integer array arr and a mapping function fn, return a new array with a transformation applied to each element.

// The returned array should be created such that returnedArray[i] = fn(arr[i], i).

// Please solve it without the built-in Array.map method.

class Solution{
   map = (arr, fn) =>{
    let new_array = [];
    for(i=0;i < arr.length;i++){
      new_array.push(fn(arr[i],i));
    }
    return new_array;
  }


}

