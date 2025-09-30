function toggleContent(id){
    let content = document.getElementById("contents_"+id)

    if(content.style.display === "none"){
        content.style.display = "block";
    }
    else{
        content.style.display = "none";
    }
};

function toggleForm(id){
    let form = document.getElementById("add_form_"+id);

    if(form.style.display === "none"){
        form.style.display = "block";
    }
    else{
        form.style.display = "none";
    }
};

/*

// Code for advanced event forum; RUS. 

function taskSwitch(time){
    let id = time+"_template"
}
*/