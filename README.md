**It was a great technical exam. I was able to troubleshoot by constantly checking:**

1. docker compose ps 
2. curl http://localhost:8080/api/health 
3. Checking logs from each individual app such as: 
	<li> docker compose logs app </li>
	<li> docker compose logs db </li>
	<li> docker compose logs nginx </li>

**Bugs found:**
1. Health check is failing due to api/health not found in app.py 
2. database names the name of the database is student_extension_requests in app.py but in init.sql its name is just extension_requests
3. Ports and IP addresses. In the app.py the host ip is home, it should be 0.0.0.0 to enable container networking.  
4. NGINX is configured to port 81 instead of port 80.


**Improvements** 
1. I've added some website UI complete with the student's names. 
<img width="1774" height="914" alt="image" src="https://github.com/user-attachments/assets/f483cb26-b5b7-46fc-b0a6-9b381fdad4ce" />
2. Added some runbooks for documentation 

**AI Usage**
1. I've used GitHub Copilot and Docker Desktop's AI on this one.
2. Whenever issues are faced, like the health check script failure, I first check the code where it's being called.
3. Like the health check script, I've noticed that it's calling api/health and when I asked AI why the result is 404 NOT FOUND, that's where it pointed out that the app.py doesn't mention the API right API call. 
