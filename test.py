import os
from supabase import create_client, Client

url: str = "https://ruiycrzcjmvfijxfwrqg.supabase.co"

key: str ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJ1aXljcnpjam12ZmlqeGZ3cnFnIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1OTk5NzM5NywiZXhwIjoyMDc1NTczMzk3fQ.2KMDkdNso50r28zZ9lhkwiP0huEdpqR3wz3J1cPI0nY"

supabase: Client = create_client(url, key)


username = "user"
password = "userpass"


response1 = (
        supabase.table("profiles").select("is_admin, email").eq("username",username).execute()
)


response2 = supabase.auth.sign_in_with_password(
        {
            "email": str(response1.data[0]["email"]),
            "password": str(password),
        }
    )

print(response2.user.aud)


