const SubCategories = document.getElementsByClassName("subcategory");
const ProductTypeContainers = document.getElementsByClassName("product-type-container");


function onHoverSubCategory(e){
    sub_category_id = e.currentTarget.id;
    
    const type_container = Array.from(ProductTypeContainers).filter((container) => {
        container.style.display = "none";

        return container.id === sub_category_id;
    })[0];

    type_container.style.display = "grid";
}

Array.from(SubCategories).forEach((sub_category) => {
    sub_category.addEventListener("mouseover", onHoverSubCategory);
});
