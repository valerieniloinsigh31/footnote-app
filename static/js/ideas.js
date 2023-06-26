const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
var deleteButtons = document.getElementsByClassName("btn-delete");
var editButtons = document.getElementsByClassName("btn-edit");
var deleteConfirm = document.getElementById("deleteConfirm");
var ideaText = document.getElementsByTagName("textarea")[0];;
var ideaForm = document.getElementById("ideaForm");
var submitideaButton = document.getElementById("submitideaButton");

// empty the footnote text after post

ideaText.value = "";

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let ideaId = e.target.getAttribute("idea_id"); // what about slug?
        deleteConfirm.href = `delete_idea/${ideaId}`;
        deleteModal.show();
    });
}

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let ideaId = e.target.getAttribute("idea_id");
        let ideaContent = document.getElementById(`idea${ideaId}`).innerText;
        ideaText.value = ideaContent;
        submitideaButton.innerText = "Update";
        ideaForm.setAttribute("action", `edit_idea/${ideaId}`);
    });
}