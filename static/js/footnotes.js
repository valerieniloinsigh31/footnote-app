const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
var deleteButtons = document.getElementsByClassName("btn-delete");
var editButtons = document.getElementsByClassName("btn-edit");
var deleteConfirm = document.getElementById("deleteConfirm");
var footnoteText = document.getElementsByTagName("textarea")[0];
var footnoteForm = document.getElementById("footnoteForm");
var submitButton = document.getElementById("submitButton");

// empty the footnote text after post

footnoteText.value = "";

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let footnoteId = e.target.getAttribute("footnote_id");
        deleteConfirm.href = `delete_footnote/${footnoteId}`;
        deleteModal.show();
    });
}

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let footnoteId = e.target.getAttribute("footnote_id");
        let footnoteContent = document.getElementById(`footnote${footnoteId}`).innerText;
        footnoteText.value = footnoteContent;
        submitButton.innerText = "Update";
        footnoteForm.setAttribute("action", `edit_footnote/${footnoteId}`);
    });
}