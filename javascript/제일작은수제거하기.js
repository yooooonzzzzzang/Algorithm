function solution(arr) {
  var answer = [];
  n = arr.length
  if (n > 1) {
    // 최소값을 찾고 -> 인덱스를 알아내서 slice를 통해 삭제
    let min_idx = arr.indexOf(Math.min.apply(null, arr))
    arr.splice(min_idx, 1)
    answer = arr
  } else {
    answer = answer.concat(-1)
  }
  return answer;
}


console.log(solution([4, 3, 2, 1]))
console.log(solution([10]))