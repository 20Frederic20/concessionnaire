# concessionnaire
--Voiture/detail--
<div class="offset-2 col-md-6 mb-3">
		<div class="col-9 card h-100 px-2">
		  <img src=" {{ voiture.image.url }} " class="card-img-top img-responsive" alt="...">
		  <div class="card-body">
		    <h5 class="card-title">Nom : &nbsp;&nbsp; {{ voiture.marque }} {{ voiture.name }} </h5>
		    <br> <br> <br>
		    <h5 class="card-title">Prix : &nbsp;&nbsp;{{ voiture.price }}  </h5>
		    <a href="{% url 'voiture:payement' voiture.pk %}" class="btn btn-info text-white offset-4">Acheter</a>
		  </div>
		</div>
	</div>