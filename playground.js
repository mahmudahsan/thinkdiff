/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

'use strict';
const assert = require('assert');
const _ = require('lodash');

const twoSum = function(nums, target) {
    const length = nums.length;
    for (let i = 0; i < length; i++){
      const _target = target - nums.shift();
      if (nums.includes(_target)) {
        return [i, nums.indexOf(_target) + i + 1]
      }
    }
};

assert(_.isEqual(twoSum([2, 7, 11, 15], 9), [0, 1])=== true)
assert(_.isEqual(twoSum([2, 0, 11, 7], 11), [1, 2]) === true)
assert(_.isEqual(twoSum([1, 3, 4, 2], 6), [2, 3]) === true)