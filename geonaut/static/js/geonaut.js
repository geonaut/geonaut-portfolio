var switches = document.getElementsByClassName('switch-bootstrap');
for(var i=0; i<switches.length; i++) {
    var retrivedValue = localStorage.getItem(switches[i].id, retrivedValue);
    var classname = switches[i].id;
    if (retrivedValue === 'no') {
        document.getElementsByClassName(classname)[0].removeAttribute('checked');
        filterPosts(document.getElementsByClassName(classname)[0].name);
    }
}

function filterPosts(id) {
    var toggleId = id + "-toggle";
    var result = document.getElementById(toggleId).checked ? 'yes' : 'no';
    localStorage.setItem(toggleId, result);
    var postIntros = document.getElementsByClassName('post-intro');
    for(var i=0; i<postIntros.length; i++) {
        if (postIntros[i].style.display === 'block' && postIntros[i].id === id) {
            postIntros[i].style.display = "none";
        } else if (postIntros[i].style.display === 'none' && postIntros[i].id === id) {
            postIntros[i].style.display = "block";
        }
    }
}