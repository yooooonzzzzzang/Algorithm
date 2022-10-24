function solution(phone_number) {
  var answer = '';
  const n = phone_number.length
  for (let i = 0; i < n; i++) {
    if (i >= n - 4) {
      answer = answer.concat(phone_number[i])
      // answer.push(phone_number[i])
    }
    else {
      answer = answer.concat('*')
      // answer.push('*')
    }
  }
  return answer;
}

console.log(solution("027774444"))