const projectName = 'survey-form';
  function getAns(){
    /* buy or rent */
    const collection1 = document.getElementsByName("property");
    for (let i = 0; i < collection1.length; i++) {
      if (collection1[i].checked == true) {
      var property_ans = i + 1;
      }
    }
    /*willing to pay */
    const collection2 = document.getElementsByName("spend");
    for (let i = 0; i < collection2.length; i++) {
      if (collection2[i].checked == true) {
        var spend_ans = i + 1;
      }
    }

    /* residence age */
    const collection3 = document.getElementsByName("propage");
    for (let i = 0; i < collection3.length; i++) {
      if (collection3[i].checked == true) {
        var propage_ans = i + 1;
      }
    }

    /* appliance age */
    const collection4 = document.getElementsByName("appage");
    for (let i = 0; i < collection4.length; i++) {
      if (collection4[i].checked == true) {
        var appage_ans = i + 1;
      }
    }

    /* electricity bill */
    const collection5 = document.getElementsByName("bill");
    for (let i = 0; i < collection5.length; i++) {
      if (collection5[i].checked == true) {
        var bill_ans = i + 1;
      }
    }
    let ans = new Array(property_ans, spend_ans, propage_ans, appage_ans, bill_ans);
    readAns(ans);
  }
  function readAns(ans){
    localStorage.setItem('MyAnswerList', JSON.stringify(ans) );
    ans_array = localStorage.getItem("MyAnswerList");
    let answers = ans_array.toString()

    var textToSave = answers;
    var textToSaveAsBlob = new Blob([textToSave], {type:"text/plain"});
    var textToSaveAsURL = window.URL.createObjectURL(textToSaveAsBlob);
    var fileNameToSaveAs = "user.txt";
 
    var downloadLink = document.createElement("a");
    downloadLink.download = fileNameToSaveAs;
    downloadLink.innerHTML = "Download File";
    downloadLink.href = textToSaveAsURL;
    downloadLink.onclick = destroyClickedElement;
    downloadLink.style.display = "none";
    document.body.appendChild(downloadLink);
 
    downloadLink.click();

  }
  function destroyClickedElement(event)
  {
    document.body.removeChild(event.target);
  }
  
