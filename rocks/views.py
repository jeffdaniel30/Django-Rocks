from django.shortcuts import render, redirect

# Create your views here.
from .models import Artist, Song
from .forms import ArtistForm

def artist_list(request):
    artists = Artist.objects.all()
    artists = artists.order_by('name')
    print(artists)
    return render(
        request, 
        'rocks/artist_list.html',
        {'artists':artists},
        )

def song_list(request):
    songs = Song.objects.all()
    return render(
        request, 
        'rocks/song_list.html',
        {'songs':songs}
        )

def song_detail(request, pk):
    song = Song.objects.get(id=pk)
    return render(request, 'rocks/song_detail.html', {'song': song})

def artist_detail(request, pk):
    try:
        artist = Artist.objects.get(id=pk)
    except:
        artist= {
            'name':"no Artist found",
            'nationality':'with id{pk}'
        }
        print(f"artist with od={pk} didnt work")
    return render(
        
        request, 
        'rocks/artist_detail.html', 
        {'artist':artist})

def artist_create(request):
    if request.method == 'POST':
        print(request.POST)
        form = ArtistForm(request.POST)
        print(form)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm()
    return render(request, 'rocks/artist_form.html', {'form':form})


def artist_edit(request, pk):
    artist = Artist.objects.get(pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_detail', pk=artist.pk)
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'rocks/artist_form.html', {'form':form})


#---------------------------------------------

def artist_delete(request, pk):
    Artist.objects.get(id=pk).delete()
    return redirect('artist_list')