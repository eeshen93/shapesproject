/*
    KEY COMPONENTS:
    "activeItem" = null until an edit button is clicked. Will contain object of item we are editing
    "list_snapshot" = Will contain previous state of list. Used for removing extra rows on list update
    
    PROCESS:
    1 - Fetch Data and build rows "buildList()"
    2 - Create Item on form submit
    3 - Edit Item click - Prefill form and change submit URL
    4 - Delete Item - Send item id to delete URL
    5 - Cross out completed shape - Event handle updated item

    NOTES:
    -- Add event handlers to "edit", "delete", "title"
    -- Render with strike through items completed
    -- Remove extra data on re-render
    -- CSRF Token
        */

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    var activeItem = null
    var list_snapshot = []

    
    buildList()
  
    

    function buildList(){
        var wrapper = document.getElementById('list-wrapper')
        //wrapper.innerHTML = ''
        
        try{
            document.getElementById('editor').remove()
        }catch(err){

        }

        var url = 'https://shapesproject.herokuapp.com/api/shapes/'

        fetch(url)
        .then((resp) => resp.json())
        .then(function(data){

            var list = data

            for (var i in list){

                try{
                    document.getElementById(`data-row-${i}`).remove()
                }catch(err){

                }

                var id = list[i].id
                var	shape = list[i].shape_type
                var	side1 = list[i].side1
                var	side2 = list[i].side2
                var	side3 = list[i].side3
                var	area = list[i].area
                var	perimeter = list[i].perimeter
                var	msg = list[i].msg
                
                var item = `<tr id='data-row-${i}'>
                    <td><span class='id'>${id}</span></td>
                    <td></td>
                    <td>${shape}</td>
                    <td>${area.toFixed(2)}</td>
                    <td>${perimeter.toFixed(2)}</td>
                    <td>${msg}</td>
                    <td><button class="edit btn btn-sm btn-outline-info">Calculate/Edit</button></td>
                    <td><button class="delete btn btn-sm btn-outline-dark">Delete</button></td>
                </tr>
                `
                
                wrapper.innerHTML+=item

            }
            //console.log('done1')
            if (list_snapshot.length > list.length){
                for (var i = list.length; i < list_snapshot.length; i++){
                    document.getElementById(`data-row-${i}`).remove()
                }
            }

            list_snapshot = list

            //console.log(list)
            for (var i in list){
                var editBtn = document.getElementsByClassName('edit')[i]
                var deleteBtn = document.getElementsByClassName('delete')[i]
                var id = document.getElementsByClassName('id')[i]
                var shape = document.getElementsByClassName('shape')[i]
            
                
                editBtn.addEventListener('click', (function(item){
                    console.log('clicked')
                    return function(){
                        editItem(item)
                    }
                })(list[i]))


                deleteBtn.addEventListener('click', (function(item){
                    return function(){
                        deleteItem(item)
                    }
                })(list[i]))



            }


        })
    }


    var form = document.getElementById('form-wrapper')
    form.addEventListener('submit', function(e){
        e.preventDefault()
        console.log('Form submitted')
        var url = 'https://shapesproject.herokuapp.com/api/create-shape/'
        if (activeItem != null){
            var url = `https://shapesproject.herokuapp.com/api/update-shape/${activeItem.id}/`
            activeItem = null
        }

        var shape_type = document.getElementById('shape_type').value
        console.log(shape_type)
        var side1 = document.getElementById('side1').value
        try{var side2=document.getElementById('side2').value}
        catch(err){var side2=0}
        try{var side3=document.getElementById('side3').value}
        catch(err){var side3=0}
        

        fetch(url, {
            method:'POST',
            headers:{
                'Content-type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'shape_type':shape_type, 'side1':side1})
        }
        ).then(function(response){
            buildList()
            
           
            document.getElementById('form').reset()
        })
    })

    var form2 = document.getElementById('form2-wrapper')
    form2.addEventListener('submit', function(e){
        e.preventDefault()
        console.log('Form submitted')
        var url = 'https://shapesproject.herokuapp.com/api/create-shape/'
        if (activeItem != null){
            var url = `https://shapesproject.herokuapp.com/api/update-shape/${activeItem.id}/`
            activeItem = null
        }

        var shape_type = document.getElementById('shape_typer').value
        
        var side1 = document.getElementById('side1r').value
        try{var side2=document.getElementById('side2r').value}
        catch(err){var side2=0}
        try{var side3=document.getElementById('side3r').value}
        catch(err){var side3=0}
        
        console.log(side1)
        fetch(url, {
            method:'POST',
            headers:{
                'Content-type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'shape_type':shape_type, 'side1':side1, 'side2':side2})
        }
        ).then(function(response){
            buildList()
            
           
            document.getElementById('form2').reset()
        })
    })
    var form3 = document.getElementById('form3-wrapper')
    form3.addEventListener('submit', function(e){
        e.preventDefault()
        console.log('Form submitted')
        var url = 'https://shapesproject.herokuapp.com/api/create-shape/'
        if (activeItem != null){
            var url = `https://shapesproject.herokuapp.com/api/update-shape/${activeItem.id}/`
            activeItem = null
        }

        var shape_type = document.getElementById('shape_typed').value
        console.log(shape_type)
        var side1 = document.getElementById('side1d').value
        try{var side2=document.getElementById('side2d').value}
        catch(err){var side2=0}
        try{var side3=document.getElementById('side3d').value}
        catch(err){var side3=0}
        

        fetch(url, {
            method:'POST',
            headers:{
                'Content-type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'shape_type':shape_type, 'side1':side1,'side2':side2})
        }
        ).then(function(response){
            buildList()
            
           
            document.getElementById('form3').reset()
        })
    })
    var form4 = document.getElementById('form4-wrapper')
    form4.addEventListener('submit', function(e){
        e.preventDefault()
        console.log('Form submitted')
        var url = 'https://shapesproject.herokuapp.com/api/create-shape/'
        if (activeItem != null){
            var url = `https://shapesproject.herokuapp.com/api/update-shape/${activeItem.id}/`
            activeItem = null
        }

        var shape_type = document.getElementById('shape_typet').value
        console.log(shape_type)
        var side1 = document.getElementById('side1t').value
        try{var side2=document.getElementById('side2t').value}
        catch(err){var side2=0}
        try{var side3=document.getElementById('side3t').value}
        catch(err){var side3=0}
        

        fetch(url, {
            method:'POST',
            headers:{
                'Content-type':'application/json',
                'X-CSRFToken':csrftoken,
            },
            body:JSON.stringify({'shape_type':shape_type, 'side1':side1, 'side2':side2, 'side3':side3})
        }
        ).then(function(response){
            buildList()
            
           
            document.getElementById('form4').reset()
        })
    })
 

    function editItem(item){
        var wrapper = document.getElementById('editform')
        console.log('Item clicked:', item)
        activeItem = item
        try{
            document.getElementById('editor').remove()
        }catch(err){

        }
        //document.getElementById('editform')
        if (activeItem.shape_type=='square'){
            var shapeform=`<h2 id='editor'>Updating Square</h2>`
            document.getElementById('shape_type').value = activeItem.shape_type
            document.getElementById('side1').value = activeItem.side1
        } else if (activeItem.shape_type=='rectangle'){
            var shapeform=`<h2 id='editor'>Updating Rectangle</h2>`
            document.getElementById('shape_typer').value = activeItem.shape_type
            document.getElementById('side1r').value = activeItem.side1
            document.getElementById('side2r').value = activeItem.side2
        } else if (activeItem.shape_type=='diamond'){
            var shapeform=`<h2 id='editor'>Updating Diamond</h2>`
            document.getElementById('shape_typed').value = activeItem.shape_type
            document.getElementById('side1d').value = activeItem.side1
            document.getElementById('side2d').value = activeItem.side2
        } else if (activeItem.shape_type=='triangle'){
            var shapeform=`<h2 id='editor'>Updating Triangle</h2>`
            document.getElementById('shape_typet').value = activeItem.shape_type
            document.getElementById('side1t').value = activeItem.side1
            document.getElementById('side2t').value = activeItem.side2
            document.getElementById('side3t').value = activeItem.side3
        }
        
        
        wrapper.innerHTML+=shapeform

    }


    function deleteItem(item){
        console.log('Delete clicked')
        fetch(`https://shapesproject.herokuapp.com/api/delete-shape/${item.id}/`, {
            method:'DELETE', 
            headers:{
                'Content-type':'application/json',
                'X-CSRFToken':csrftoken,
            }
        }).then((response) => {
            buildList()
            
            
        })
    }




