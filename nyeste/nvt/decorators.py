from django.shortcuts import redirect


def adminonly(view_func):
    def wrapper_func(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
        # if request.user.profile.admin==False:
        #     return redirect('home')
        # else:
        #     return view_func(request,*args, **kwargs)

    return wrapper_func


def staffonly(view_func):
    def wrapper_func(request, *args, **kwargs):
        return view_func(request, *args, **kwargs)
        # if request.user.profile.admin==True:
        #     return redirect('home')
        # elif request.user.profile.status=="alive":
        #     return view_func(request,*args, **kwargs)
        # else:
        #     return redirect('home')

    return wrapper_func
