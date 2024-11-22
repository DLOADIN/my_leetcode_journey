// Given two promises promise1 and promise2, return a new promise. promise1 and promise2 will both resolve with a number. The returned promise should resolve with the sum of the two numbers.

class Solution{
  addTwoPromises = async function(promise1, promise2) {
    const results = await Promise.all([promise1, promise2]);

  // Ensure both results are numbers
  if (typeof results[0] !== 'number' || typeof results[1] !== 'number') {
      throw new Error("returned promise should resolve with a number");
  }

  // Return the sum of the two numbers
  return results[0] + results[1];
};
}