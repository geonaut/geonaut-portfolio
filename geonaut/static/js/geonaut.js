// $(function () {
//     var postIntro = document.getElementsByClassName('post-intro');
//     console.log(postIntro);
//     $("#tech-switch").click(function () {
//     $("#Technical").toggle();
//     });
// });

// var info = document.getElementsByClassName('Personal');

// document.getElementsByClassName('Personal')[0].removeAttribute('checked');
// localStorage.setItem('personal-toggle', 'no');
// var ids = '';
// get all switches
var switches = document.getElementsByClassName('switch-bootstrap');
// iterate through switches
for(var i=0; i<switches.length; i++) {
    // for each switch, get any stored value
    var retrivedValue = localStorage.getItem(switches[i].id, retrivedValue);
    var classname = switches[i].id;
    // console.log("retrivedValue is:" + retrivedValue);
    // console.log("classname is:" + classname);
    // if the store value = no
    if (retrivedValue === 'no') {
        // strip checked
        document.getElementsByClassName(classname)[0].removeAttribute('checked');
        filterPosts(document.getElementsByClassName(classname)[0].name);
    } else {
        // document.getElementsByClassName('Personal').setAttribute('checked', 'checked');
    }
    // ids += switches[i].id
}

// localStorage.setItem('FilterPersonal', 'yes');
// var retrivedValue = localStorage.getItem('personal-toggle', retrivedValue);
// console.log(info)
// console.log("retrivedValue is:" + retrivedValue);
// console.log(switches);
// console.log(ids);
// console.log(localStorage);

function filterPosts(id) {
    var toggleId = id + "-toggle";
    // console.log(toggleId);
    var result = document.getElementById(toggleId).checked ? 'yes' : 'no';
    localStorage.setItem(toggleId, result);
    // console.log(result);
    var postIntros = document.getElementsByClassName('post-intro');
    for(var i=0; i<postIntros.length; i++) {
        if (postIntros[i].style.display === 'block' && postIntros[i].id === id) {
            postIntros[i].style.display = "none";
        } else if (postIntros[i].style.display === 'none' && postIntros[i].id === id) {
            postIntros[i].style.display = "block";
        }
    }
}