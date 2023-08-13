using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Collections.Concurrent;
using Thrid_angle.Database.RestAPI.DTO;
using Microsoft.Extensions.Hosting;

namespace Thrid_angle.Database.RestAPI.Mehtods
{
    public class HelperMethodsDatabase 
    {

        ConcurrentDictionary<Guid, Guid> _IdOrderCard;
        ConcurrentDictionary<Guid, int> _NumberCard;

        public HelperMethodsDatabase() 
        {

            _NumberCard = new ConcurrentDictionary<Guid, int>();

            _IdOrderCard = new ConcurrentDictionary<Guid, Guid>();

        }  


         public  Guid  BasketNewGuidOrderCard(Guid IdUser, bool NewNumberOrderCard)
        {
          
            Guid g = new Guid();
         
            
            if (_IdOrderCard.ContainsKey(IdUser)&NewNumberOrderCard==false) 
            {
                g = _IdOrderCard[IdUser];
                
            }

            if (_IdOrderCard.ContainsKey(IdUser)&NewNumberOrderCard  )
            {
                Guid guid = Guid.NewGuid();
                _IdOrderCard[IdUser] = guid;
                g = _IdOrderCard[IdUser]; 
              

            }

            if (_IdOrderCard.ContainsKey(IdUser)!=true) 
            {
                _IdOrderCard.TryAdd(IdUser, Guid.NewGuid());
               g = _IdOrderCard[IdUser];

               

            }

            return g ;


        }





        public int  BasketNewNumberCard(Guid IdUser, bool NewNumberOrderCard)
        {

           
            int i = 0;

            if (_NumberCard.ContainsKey(IdUser) & NewNumberOrderCard == false)
            {
               
                i = _NumberCard[IdUser];
            }

            if (_NumberCard.ContainsKey(IdUser) & NewNumberOrderCard)
            {
               
                _NumberCard[IdUser] = _NumberCard[IdUser] + 1;
                i = _NumberCard[IdUser];

            }

            if (_NumberCard.ContainsKey(IdUser) != true)
            {

                _NumberCard.TryAdd(IdUser, 1);

                i = _NumberCard[IdUser];


            }

            return i;


        }























    }
}
