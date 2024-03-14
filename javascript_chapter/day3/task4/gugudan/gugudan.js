function gugudan() {
  for (var i = 1; i < 10; i++) {
    for (var j = 2; j < 10; j++) {
      var result = `${j} * ${i} = ${j * i}`;
      console.log(result);
      const span = document.createElement("span");
      span.textContent = `${j} * ${i} = ${j * i}`;
      document.body.append(span);
    }
    const p = document.createElement("p");
    document.body.append(p);
  }
}

window.onload = gugudan;
