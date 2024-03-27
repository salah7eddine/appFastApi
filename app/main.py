from fastapi import FastAPI, Response, status, HTTPException
from random import randrange

from app.model.Post import Post
from app.db.connectDB import get_conn



app = FastAPI()


my_posts  = [{"title": 'title 1', "content": "content 1", "id": 1}, {"title": 'title 2', "content": "content 2", "id": 2}]




# request Get method url : "/"
@app.get("/")
def root():
    return {"message": "Hi Salah, Hello Hamza, Hi Meryem !!"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.get("/v1/posts")
def root():
    with get_conn() as conn:
        conn.execute("""SELECT * FROM posts""")
        posts = conn.fetchall()
        print(posts)
    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    return {"status":"Success", "message": post_dict}

def find_post(id):
    for p in my_posts:
        if p["id"] == id :
            return p

    
def find_index_post(id): 
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i

@app.get("/posts/latest")
def get_lastest_post():
    post = my_posts[len(my_posts)-1]
    return {"detail" : post}

@app.get("/posts/{id}")    
def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"for this id {id} post Not found")
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return { 'error': f"for this id {id} post Not found"}
    return {"detail": post}


@app.delete("/posts/{id}", status_code= status.HTTP_204_NO_CONTENT)
def delete_post(id:int):
    # deleting post
    # find the index in the array that has required ID
    # my_posts pop
     
     index = find_index_post(id)
     if index == None:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id}, is not available to be deleted.")
     my_posts.pop(index)
     return Response(status_code= status.HTTP_204_NO_CONTENT)

@app.put("/posts/{id}")
def update_post(id:int , post:Post):
   # check if the given id is present
    index = find_index_post(id)
    if index == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id:{id}, is not available to be deleted.")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    
    return {'data': post_dict }
