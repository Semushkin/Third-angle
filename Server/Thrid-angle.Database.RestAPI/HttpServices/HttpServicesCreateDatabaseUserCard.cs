using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Thrid_angle.Database.RestAPI.DTO;
using System.Net.Http;
using System.Text.Json;
using static System.Net.Mime.MediaTypeNames;
using System.Net.Http.Json;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.Net.Http.Headers;

namespace Thrid_angle.Database.RestAPI.HttpServices
{
    internal class HttpServicesCreateDatabaseUserCard
    {

        private readonly IHttpClientFactory _httpClientFactory = null!;

        HttpServicesCreateDatabaseUserCard(IHttpClientFactory httpClientFactory) => (_httpClientFactory) = httpClientFactory;


        public async Task<UserCard> UserCardHttpSevicesGET(string UserName, string SurnameUser, string RoleUser, string FloorUser, int AgeUser, string AddressUser, string TelephoneUser, string EmailUser, string LoginUser, string PasswordUser, DateTime DateCreationUser, DateTime UpdateDateUser)
        {
            using HttpClient client = _httpClientFactory.CreateClient();

         try 
            {
                UserCard? _UserCard = await client.GetFromJsonAsync<UserCard>(
                    $"https://localhost:5000/ServicesRest/CreateDatabaseUserCard?{UserName}/{SurnameUser}/{RoleUser}/{FloorUser}/{AgeUser}/{AddressUser}/{TelephoneUser}/{EmailUser}/{LoginUser}/{PasswordUser}/{DateCreationUser}/{UpdateDateUser}",
                    new JsonSerializerOptions(JsonSerializerDefaults.Web));

                return _UserCard;


            }

            catch (Exception ex) 
            {
             return new UserCard();
            
            }



        }



       // public class BasicModel : PageModel
       // {
       //     private readonly IHttpClientFactory _httpClientFactory;
       //
       //     public BasicModel(IHttpClientFactory httpClientFactory) =>
       //         _httpClientFactory = httpClientFactory;
       //
       //     public IEnumerable<GitHubBranch>? GitHubBranches { get; set; }
       //
       //     public async Task OnGet()
       //     {
       //         var httpRequestMessage = new HttpRequestMessage(
       //             HttpMethod.Get,
       //             "https://api.github.com/repos/dotnet/AspNetCore.Docs/branches")
       //         {
       //             Headers =
       //     {
       //         { HeaderNames.Accept, "application/vnd.github.v3+json" },
       //         { HeaderNames.UserAgent, "HttpRequestsSample" }
       //     }
       //         };
       //
       //         var httpClient = _httpClientFactory.CreateClient();
       //         var httpResponseMessage = await httpClient.SendAsync(httpRequestMessage);
       //
       //         if (httpResponseMessage.IsSuccessStatusCode)
       //         {
       //             using var contentStream =
       //                 await httpResponseMessage.Content.ReadAsStreamAsync();
       //
       //             GitHubBranches = await JsonSerializer.DeserializeAsync
       //                 <IEnumerable<GitHubBranch>>(contentStream);
       //         }
       //     }
       // }



















    }
}
