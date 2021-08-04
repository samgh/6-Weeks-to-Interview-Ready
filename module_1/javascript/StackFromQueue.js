/*
 *   Title: Stack from Queues
 *   Leetcode Link: https://leetcode.com/problems/implement-stack-using-queues/
 *
 *   Problem: Implement a LIFO stack with basic operations using 2 FIFO queues.
 *
 *   Execution: node StackFromQueuenjs
 */

var MyStack = function() {
    // Implementing a queue like this:
    // https://www.javascripttutorial.net/javascript-queue/
    this.queue = [];
};

/**
 * Push an item onto the stack
 *
 * @param {number} x
 * @return {void}
 */
MyStack.prototype.push = function(x) {
    // We are going to just create a new queue here so we're using 2 queues
    // _at a time_. If we want to be more precise, we could allocate two
    // queues at the beginning and just alternate between which we're using
    // as the primary and secondary queues
    var newQueue = []

    // Maintain our queue in stack order. To add an item to the end of the
    // queue we add that first before everything else
    newQueue.push(x);
    this.queue.forEach(function(i) {
        newQueue.push(i);
    });

    // newQueue now contains all elements in proper order
    this.queue = newQueue;
};

/**
 * Remove the most recently added element from the stack
 *
 * @return {number}
 */
MyStack.prototype.pop = function() {
    // We've handled all the logic while pushing so this is easy
    return this.queue.shift();
};

/**
 * Return the top element of stack without removing it
 *
 * @return {number}
 */
MyStack.prototype.top = function() {
    return this.queue[0];
};

/**
 * Return true if stack is empty
 *
 * @return {boolean}
 */
MyStack.prototype.empty = function() {
    return this.queue.length === 0;
};

var tester = function() {
    var stack = new MyStack();
    stack.push(1);
    stack.push(2);
    stack.push(3);
    stack.push(4);

    console.log(stack.queue);
    console.log(stack.pop());
    console.log(stack.queue);
}

tester();
