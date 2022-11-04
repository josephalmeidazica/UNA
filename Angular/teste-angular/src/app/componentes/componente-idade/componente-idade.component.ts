import { Component, OnInit, Input } from '@angular/core';
import { FormBuilder} from '@angular/forms';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-componente-idade',
  templateUrl: './componente-idade.component.html',
  styleUrls: ['./componente-idade.component.css']
})
export class ComponenteIdadeComponent implements OnInit {

  idadeForm = this.formBuilder.group({
    nasc: 0
  });

  idade = 0;

  constructor(private formBuilder: FormBuilder,
    private route: ActivatedRoute) {}
   onSubmit() {
    let agora = new Date
    let ano = agora.getFullYear()
    if(this.idadeForm.value.nasc != null)
    {
      this.idade = ano - this.idadeForm.value.nasc;
    }
  }
  ngOnInit(): void {
  }

}
