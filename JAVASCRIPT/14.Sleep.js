// Given a positive integer millis, write an asynchronous function that sleeps for millis milliseconds. It can resolve any value.

class Solution{
  async sleep(millis, value) {
    return new Promise(resolve => setTimeout(() => resolve(value), millis));
  }
}