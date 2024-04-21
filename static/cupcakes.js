$('.delete-cupcake').click(deleteCupcake)

async function deleteCupcake(){
    const id = $(this).data('id')
    await axios.delete(`/api/cupcakes/${id}`)
    $(this).parent().remove()
}
axios.delete()

$('.add-cupcake').click(addCupcake)
async function addCupcake(){
    
    let flavor = $('#flavor').val();
    let size = $('#size').val();
    let rating = $('#rating').val();
    let image = $('#image').val();

    const newCupcakeResponse = await axios.post('/api/cupcakes', {
        flavor,
        rating,
        size,
        image
    });

    let newCupcake = $(addCupcakeToPageHTML(newCupcakeResponse.data.cupcake));
    $('#cupcake-list').append(newCupcake);
    $('#new-cupcake-form').trigger("reset");
}

async function addCupcakeToPageHTML(cupcake){
    return `
    <div class="column p-5">
        <h3 class="row">${cupcake.flavor}</h3>
        <img class="row img-thumbnail" src="${cupcake.image}">
        <p><b>Size:</b> ${cupcake.size} | <b>Rating:</b> ${cupcake.rating}</p>
        <button type="button" class="delete-cupcake row btn btn-danger btn-sm m-1" data-id="${cupcake.id }">Delete</button>
    </div>`;
}


