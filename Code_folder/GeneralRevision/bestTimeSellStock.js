function bestTime(prices){
    let max_profit = -Infinity
    let current_price = prices[0]
    for(let i =1; i<prices.length ; i++){

        let profit = prices[i] - current_price
        if (prices[i] < current_price){
            current_price = prices[i]
        }
        else{
            if (profit > max_profit){
                max_profit = profit
            }
        }
    
    }
    return max_profit

}

input = [3,2,5,8,1,4]

console.log(bestTime(input))



function bestTime2(prices) {
    let max_profit = 0;  // start with 0
    let min_price = prices[0];

    for (let i = 1; i < prices.length; i++) {
        const profit = prices[i] - min_price;

        max_profit = Math.max(max_profit, profit);
        min_price = Math.min(min_price, prices[i]);
    }

    return max_profit;
}

const input2 = [3, 2, 5, 8, 1, 4];
console.log(bestTime2(input2));  // Output: 6 (Buy at 2, sell at 8)


function bestTime1(prices) {
    let l = 0; // buy pointer
    let r = 1; // sell pointer
    let max_profit = 0;

    while (r < prices.length) {
        if (prices[r] > prices[l]) {
            let profit = prices[r] - prices[l];
            max_profit = Math.max(max_profit, profit);
        } else {
            l = r; // lower buy price found
        }
        r++;
    }

    return max_profit;
}

const input1 = [3, 2, 5, 8, 1, 4];
console.log(bestTime1(input1));  // Output: 6 (buy at 2, sell at 8)
